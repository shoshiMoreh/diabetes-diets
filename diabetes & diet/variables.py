import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
import  diabetes as d
import numpy as np

df = pd.read_csv('./data/diabetes_prediction_dataset.csv')
X_columns = 'gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level'
X, y = d.scalerData()
X_train, X_test, y_train, y_test = train_test_split(X, y.values, test_size=0.2, random_state=42)