import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
import variables as var
import numpy as np

def oridinalWordsToNum():
    # הפיכת הנתונים המילוניים למספרים
    oe = OrdinalEncoder()
    oe.fit(var.df.loc[:, ['gender', 'smoking_history']].values)
    var.df.loc[:, ['gender', 'smoking_history']] = oe.transform(var.df.loc[:, ['gender', 'smoking_history']])

def scalerData():
    # נרמול הנתונים
    y = var.df.diabetes
    scaler = StandardScaler()
    scaler.fit(var.df.loc[:, var.X_columns])
    X = scaler.transform(var.df.loc[:, var.X_columns])
    return X, y

def trainTheModel():
    LR = 0.0001
    # הכנת המודל + שכבות
    tf.random.set_seed(42)
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=8),
        tf.keras.layers.Dense(8, activation=tf.keras.activations.tanh),
        tf.keras.layers.Dense(16, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(16, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(64, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(128, activation=tf.keras.activations.tanh),
        tf.keras.layers.Dense(64, activation=tf.keras.activations.tanh),
        tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(16, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(8, activation=tf.keras.activations.relu),
        tf.keras.layers.Dense(4, activation=tf.keras.activations.tanh),
        # tf.keras.layers.Dense(2, activation=tf.keras.activations.tanh),
        tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid)
    ])
    # קימפול המודל
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LR),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['accuracy'])
    # אימון המודל
    history = model.fit(var.X_train, var.y_train, epochs=20)
    # צפיית הנתונים על המבחן
    model.evaluate(var.X_test, var.y_test)
    model.save('./models/diabetes.keras')

def inputData(to_pred):
    oe = OrdinalEncoder()
    oe.fit(var.df.loc[:, ['gender', 'smoking_history']].values)
    var.df.loc[:, ['gender', 'smoking_history']] = oe.transform(var.df.loc[:, ['gender', 'smoking_history']])
    to_pred[['gender', 'smoking_history']] = oe.transform(to_pred[['gender', 'smoking_history']])
    print("אחרי קידוד")
    print(to_pred)
    scaler = StandardScaler()
    scaler.fit(var.df.loc[:, var.X_columns])
    to_pred.loc[:, var.X_columns] = scaler.transform(to_pred.loc[:, var.X_columns])
    print("אחרי נרמול")
    print(to_pred)

def begin():
    # קריאת הדאטה ל df
            #var.df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
    # print(df.head())
    # # בדיקה האם יש לנו תאים ריקים בדאטה
    # print(df.isnull().sum())
    oridinalWordsToNum()
    print("קידוד:")
    print(var.df.head())
            #var.X_columns = 'gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'
    X, y = scalerData()
    print("נרמול:")
    print(X[1])
    # חלוקת הדאטה לאימון ומבחן
            #X_train, X_test, y_train, y_test = train_test_split(X, y.values, test_size=0.2, random_state=42)
    #trainTheModel()
    # קריאה שוב למסד נתונים לצורך בדיקת המודל
    var.df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
    # to_pred = df.iloc[[10000], :8]
    # שושי
    # to_pred = {'gender':"Female", 'age':20, 'hypertension':0, 'heart_disease':0, 'smoking_history':"never", 'bmi':19.48, 'HbA1c_level':4, 'blood_glucose_level':80}
    # יסמין
    # to_pred = {'gender':"Female", 'age':20, 'hypertension':0, 'heart_disease':0, 'smoking_history':"never", 'bmi':21, 'HbA1c_level':4.2, 'blood_glucose_level':80}
    to_pred = {'gender':"Female", 'age':20.4, 'hypertension':0, 'heart_disease':0, 'smoking_history':"ever", 'bmi':27.73,
               'HbA1c_level':6, 'blood_glucose_level':150}

    var.df = var.df._append(to_pred, ignore_index=True)
    to_pred = var.df.iloc[[-1],:8]
    print("נתונים לצפייה:")
    print(to_pred)
    inputData(to_pred)
    from tensorflow.keras.models import load_model
    MStroke = load_model('./models/diabetes.keras')
    print(MStroke.predict(to_pred))

begin()
def bmi(kg, high):
    return kg / ((high/100) ** 2)

print(bmi(45, 152))