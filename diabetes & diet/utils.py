import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import tensorflow as tf

def predict(model_path, personal_details):
    print("hi predict")
    MStroke = load_model(model_path)
    print("הסיכויים שלך:")
    print(MStroke.predict(personal_details))
    # return personal_details
    return MStroke.predict(personal_details)


def create_personal_data(df_path, personal_details):
    print("hi create personal data")
    df = pd.read_csv(df_path)
    df = df._append(personal_details, ignore_index=True)
    personal_details = df.iloc[[-1], :8]
    return personal_details, df


def all(df_path, personal_details):
    print("hi all")
    df = pd.read_csv(df_path)
    oridinalWordsToNum(df)
    X_columns = 'gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'
    X, y = scalerData(df, X_columns)
    personal_details, df = create_personal_data(df_path, personal_details)
    print("dfgh")
    personal_details = inputData(df, personal_details, X_columns)
    return predict('./models/diabetes.keras', personal_details)


def oridinalWordsToNum(df):
    print("hi ordinal")
    # הפיכת הנתונים המילוניים למספרים
    oe = OrdinalEncoder()
    oe.fit(df.loc[:, ['gender', 'smoking_history']].values)
    df.loc[:, ['gender', 'smoking_history']] = oe.transform(df.loc[:, ['gender', 'smoking_history']])
    return df


def scalerData(df, X_columns):
    print("hi scalar data")
    # נרמול הנתונים
    # y = df.diabetes
    y = 0
    scaler = StandardScaler()
    scaler.fit(df.loc[:, X_columns])
    X = scaler.transform(df.loc[:, X_columns])
    return X, y


def inputData(df, personal_details, X_columns):
    print("hi input data")
    oe = OrdinalEncoder()
    oe.fit(df.loc[:, ['gender', 'smoking_history']].values)
    df.loc[:, ['gender', 'smoking_history']] = oe.transform(df.loc[:, ['gender', 'smoking_history']])
    personal_details[['gender', 'smoking_history']] = oe.transform(personal_details[['gender', 'smoking_history']])
    print("אחרי קידוד")
    print(personal_details)
    scaler = StandardScaler()
    scaler.fit(df.loc[:, X_columns])
    personal_details.loc[:, X_columns] = scaler.transform(personal_details.loc[:, X_columns])
    print("אחרי נרמול")
    print(personal_details)
    return personal_details

def bmi(kg, high):
    return kg / ((high/100) ** 2)


# if __name__ == '__main__':
#     all('../data/diabetes_prediction_dataset.csv',
#         {'gender': "Female", 'age': 20.4, 'hypertension': 0, 'heart_disease': 0, 'smoking_history': "ever",
#          'bmi': bmi(45, 152),
#          'HbA1c_level': 6, 'blood_glucose_level': 150})
