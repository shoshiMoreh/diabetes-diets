import numpy as np
import pandas as pd
import pulp
from pulp import *

def all():
    data = pd.read_csv('nutrition.csv').drop('Unnamed: 0', axis=1)
    # print(data.head())
    X = 'Name', 'carbohydrate', 'calories', 'total_fat', 'protein'
    data = data.loc[:, X]
    print(data.head())
    n = ""
    for i in range(0, data.shape[0]):
        for j in range(1, data.shape[1]):
            d = data.iloc[i, j]
            for s in str(d):
                if s == "." or s.isnumeric():
                    n += s
            n = float(n)
            data.iloc[i, j] = n
            n = ""
    print(data.head())
    # מערך של כל הימים בשבוע
    daysWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    # יוצר מערך שמכיל 8 חלוקות של מספרים, בעצם לוקח את הטווח ומחלק ל 8 מספרים ששווים ברווחיהם
    numOfValue = np.linspace(0, len(data), 8).astype(int)
    numOfValue[-1] = numOfValue[-1] - 1
    daysData = randomDataset(data, numOfValue, daysWeek)
    return daysWeek, daysData


# פונקציה המחלקת את הדאטה אחרי ערבוב ל 7 ימי השבוע
def randomDataset(data, numOfValue, daysWeek):
    mixData = data.sample(frac=1).reset_index().drop('index', axis=1)
    dataDays = []
    for s in range(len(numOfValue) - 1):
        dataDays.append(mixData.loc[numOfValue[s]:numOfValue[s + 1]])
    return dict(zip(daysWeek, dataDays))


def buildNutritionalValues(kg, calories):
    protiens = kg * 4  # חלבונים
    resCalorias = calories - protiens  # תוצאות הקלוריות
    carbohydrates = calories / 2  # פחמימות
    fats = calories - carbohydrates - protiens  # שומנים
    res = {'protien calories': protiens, 'carbohydrates calories': carbohydrates, 'fat calories': fats}
    return res

def extractGrams(table):
    protiens = table['protien calories'] / 4
    carbohydrates = table['carbohydrates calories'] / 4
    fats = table['fat calories'] / 9
    res = {'protien grams': protiens, 'carbohydrates grams': carbohydrates, 'fat grams': fats}
    return res

def model(prob, day, kg, calories, daysData):
    print("start")
    G = extractGrams(buildNutritionalValues(kg, calories))
    C = G['carbohydrates grams']
    P = G['protien grams']
    F = G['fat grams']
    dayData = daysData[day]
    dayData = dayData[dayData.calories != 0]
    food = dayData.Name.tolist()
    for f in range(len(food)):
        a = food[f]
        food[f] = a[:15]
    c = dayData.calories.tolist()
    # מכניסה למשתנה X מילון של משתני ההחלטה
    x = pulp.LpVariable.dicts("x", indices=food, lowBound=0, upBound=1.5, cat='Continuous', indexStart=[])
    e = dayData.carbohydrate.tolist()
    f = dayData.total_fat.tolist()
    p = dayData.protein.tolist()
    # הוספת אילוצים
    prob += pulp.lpSum([x[food[i]] * c[i] for i in range(len(food))])
    prob += pulp.lpSum([x[food[i]] * e[i] for i in range(len(x))]) >= C
    prob += pulp.lpSum([x[food[i]] * f[i] for i in range(len(x))]) >= F
    prob += pulp.lpSum([x[food[i]] * p[i] for i in range(len(x))]) >= P
    prob.solve()
    variables = []
    values = []
    for v in prob.variables():
        variable = v.name
        value = v.varValue
        variables.append(variable)
        values.append(value)
    if (len(food) > len(values)):
        food = food[:len(values)]
    # עיגול הנתונים ל 2 ספרות אחרי הנקודה והפיכתם לעשרוני- float
    values = np.array(values).round(2).astype(float)
    sol = pd.DataFrame(np.array([food, values]).T, columns=['Food', 'Quantity'])
    sol['Quantity'] = sol.Quantity.astype(float)
    sol = sol[sol['Quantity'] != 0.0]
    sol.Quantity = sol.Quantity * 100
    sol = sol.rename(columns={'Quantity': 'Quantity (g)'})
    print("end")
    return sol

def totalModel(kg, calories):
    daysWeek, daysData = all()
    result = []
    for day in daysWeek:
        prob = pulp.LpProblem("diet", LpMinimize)
        print('building a model for day %s \n' % (day))
        sol = model(prob, day, kg, calories, daysData)
        result.append(sol)
    return dict(zip(daysWeek, result))

def numCalories(kg, h, age, gender):
    if(gender==1): # גבר
        return (10*kg) + (6.25*h) - (5*age) +5
    else:
        return (10*kg) + (6.25*h) - (5*age) -161


# print(totalModel(70, numCalories(80,170, 35, 0)))