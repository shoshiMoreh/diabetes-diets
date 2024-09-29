import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# קריאת הדאטה ל df
df = pd.read_csv('./data/heart_attack_prediction_dataset.csv')
# print(df.head())
# בדיקה האם יש לנו תאים ריקים בדאטה
# print(df.isnull().sum())

from sklearn.preprocessing import OrdinalEncoder

# הפיכת הנתונים המילוניים למספרים
oe = OrdinalEncoder()
oe.fit(df.loc[:, ['Sex', 'Diet', 'Country', 'Continent', 'Hemisphere']].values)
df.loc[:, ['Sex', 'Diet', 'Country', 'Continent', 'Hemisphere']] = oe.transform(df.loc[:, ['Sex', 'Diet', 'Country', 'Continent', 'Hemisphere']])
for i in range(0, df.shape[0]):
    systolic, diastolic = df.loc[i, 'Blood Pressure'].split('/')
    systolic = int(systolic)
    diastolic = int(diastolic)
    df.loc[i, 'Blood Pressure'] = (2 * diastolic + systolic) / 3
print("hutjnxrnpruet5c")
print(df.head())
# נרמול הנתונים
X_columns = 'Age', 'Sex', 'Cholesterol', 'Blood Pressure', 'Heart Rate','Diabetes','Family History', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Exercise Hours Per Week', 'Diet', 'Previous Heart Problems', 'Medication Use', 'Stress Level', 'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides', 'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'Country', 'Continent', 'Hemisphere'
y = df["Heart Attack Risk"]
scaler = StandardScaler()
scaler.fit(df.loc[:, X_columns])
X = scaler.transform(df.loc[:, X_columns])
# print(X[1])

# חלוקת הדאטה לאימון ומבחן
X_train, X_test, y_train, y_test = train_test_split(X, y.values, test_size=0.2, random_state=42)

LR = 0.01

# הכנת המודל + שכבות
tf.random.set_seed(42)
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=24),
    # tf.keras.layers.Dense(32, activation=tf.keras.activations.tanh),
    # tf.keras.layers.Dropout(rate=0.5),
    # tf.keras.layers.Dense(20, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(64, activation=tf.keras.activations.tanh),
    # tf.keras.layers.Dense(64, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(128, activation=tf.keras.activations.tanh),
    # tf.keras.layers.Dense(128, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(256, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(256, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(64, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(64, activation=tf.keras.activations.tanh),
    # tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(32, activation=tf.keras.activations.relu),
    # tf.keras.layers.Dense(32, activation=tf.keras.activations.tanh),
    # tf.keras.layers.Dense(16, activation=tf.keras.activations.tanh),
tf.keras.layers.Dense(16, activation=tf.keras.activations.tanh),
# tf.keras.layers.Dropout(rate=0.5),
    tf.keras.layers.Dense(8, activation=tf.keras.activations.tanh),
# tf.keras.layers.Dropout(rate=0.5),
#     tf.keras.layers.Dense(4, activation=tf.keras.activations.tanh),
# tf.keras.layers.Dense(4, activation=tf.keras.activations.tanh),
tf.keras.layers.Dense(4, activation=tf.keras.activations.tanh),
    # tf.keras.layers.Dense(2, activation=tf.keras.activations.relu),
    tf.keras.layers.Dense(1, activation=tf.keras.activations.sigmoid)
])

# קימפול המודל
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LR),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['accuracy'])

# אימון המודל
history = model.fit(X_train, y_train, epochs=15)
# צפיית הנתונים על המבחן
model.evaluate(X_test, y_test)

# model.save('./models/diabetes.keras')
# df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
# to_pred = df.iloc[[10000], :8]
# print(to_pred)
#
# to_pred[['gender', 'smoking_history']] = oe.transform(to_pred[['gender', 'smoking_history']])
# to_pred.loc[:, X_columns] = scaler.transform(to_pred.loc[:, X_columns])
# print(to_pred)
#
# from tensorflow.keras.models import load_model
# MStroke = load_model('./models/diabetes.keras')
# print(MStroke.predict(to_pred))
#
