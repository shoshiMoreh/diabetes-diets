from diet import totalModel
from utils import all, bmi
from diet import numCalories
def newUser(kg, h, age, gender):
    """
    מקבלת פרמטרים של משתמש חדש, שולחת למודל ומחזירה במקרה של תוצאה גבוהה תפריט
    במקרה וסיכוייו לחלות נמוכים הפונקציה תחזירה הודעה מתאימה
    :param kg:
    :param h:
    :param age:
    :param gender:
    :return:
    """

#1. אם הוא משתמש חדש יש להוסיף אותו למסד הנתונים, לשלוח למודל ואם התוצאה היא קרובה ל-1 לשלוח לאלגוריתם
#2. אם הוא משתמש קיים אז אם הוא רוצה אז יש לו אפשרות להחליף דיאטה- הוצאת הנתונים מהמסד ושליחה חוזרת לאלגוריתם

# להוסיף משתמש ואז להחזיר את ה ID וכשקוראים למודל לשלוח את ה ID

def sendModel(user, diet):
    if user.get("heartDisease") == False and user.get("hypertension") == False:
        n = all('./data/diabetes_prediction_dataset.csv',
                {'gender': user.get("gender"), 'age': user.get("age"), 'hypertension': 0,
                 'heart_disease': 0, 'smoking_history': user.get("smokingHistory"),
                 'bmi': bmi(user.get("kg"), user.get("high")),
                 'HbA1c_level': user.get("hba1cLevel"), 'blood_glucose_level': user.get("bloodGlucoseLevel")})
    elif user.get("heartDisease") == True and user.get("hypertension") == False:
        n = all('./data/diabetes_prediction_dataset.csv',
                {'gender': user.get("gender"), 'age': user.get("age"), 'hypertension': 0,
                 'heart_disease': 1, 'smoking_history': user.get("smokingHistory"),
                 'bmi': bmi(user.get("kg"), user.get("high")),
                 'HbA1c_level': user.get("hba1cLevel"), 'blood_glucose_level': user.get("bloodGlucoseLevel")})
    elif user.get("heartDisease") == False and user.get("hypertension") == True:
        n = all('./data/diabetes_prediction_dataset.csv',
                {'gender': user.get("gender"), 'age': user.get("age"), 'hypertension': 1,
                 'heart_disease': 0, 'smoking_history': user.get("smokingHistory"),
                 'bmi': bmi(user.get("kg"), user.get("high")),
                 'HbA1c_level': user.get("hba1cLevel"), 'blood_glucose_level': user.get("bloodGlucoseLevel")})
    else:
        n = all('./data/diabetes_prediction_dataset.csv',
                {'gender': user.get("gender"), 'age': user.get("age"), 'hypertension': 1,
                 'heart_disease': 1, 'smoking_history': user.get("smokingHistory"),
                 'bmi': bmi(user.get("kg"), user.get("high")),
                 'HbA1c_level': user.get("hba1cLevel"), 'blood_glucose_level': user.get("bloodGlucoseLevel")})
    n = n * 100
    print("חזרה מהמודל")
    print(n)
    print(type(n))
    a = n.item()
    a = str(a)
    m = ""

    for i in range(0, len(a)):
        if a[i] != ".":
            m += a[i]
        else:
            m += a[i]
            m += a[i+1]
            break
    print(m)
    diet['chanceDiabetes'] = float(m)
    print(diet['chanceDiabetes'])
    if n > 50:
        if user.get("gender") == "Male":
            d = totalModel(user.get("kg"), numCalories(user.get("kg"), user.get("high"), user.get("age"), 1))
        else:
            d = totalModel(user.get("kg"), numCalories(user.get("kg"), user.get("high"), user.get("age"), 2))
        if d:
            print("הסוג של הנתונים")
            print(type(d))
            print(d)
            days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            print(type((d['Sunday'])['Food']))
            for day in days_of_week:
                diet[day.lower()] = []
                for index, row in d[day].iterrows():
                    row['Quantity (g)'] = int(row['Quantity (g)'])
                    print(row)  # הוספת הדפסה לבדיקת מבנה השורה
                    diet[day.lower()].append([str(row['Food']), str(row['Quantity (g)'])])
    return diet









def yasminush():
    print(f"""menu:
    1: i want to send heart
    2: i want to say: you sweet!!!
    3: i want to say: shoshiiiiiiiiiiiiiiiii
    4: i want to cry
    5: i want to ask question
    6: to end.....""")
    a = input()
    while a != "6":
        if a == "1":
            print("❤️")
        elif a == "2":
            print("☺️")
        elif a == "3":
            print("Yasminushhhhhhhhhhhhhhhh")
        elif a == "4":
            print("😭")
        elif a == "5":
            print("and back to you??")
        a = input()
    print("It's always nice to talk to you!!!")

# yasminush()

