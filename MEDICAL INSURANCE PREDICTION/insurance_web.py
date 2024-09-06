import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import pickle

#Load data
insurance = pd.read_csv('insurance.csv')

insurance_model = pickle.load(open('insurance_model.pkl','rb'))

insurance['log_charges'] = np.log2(insurance['charges'])
insurance['is_smoker'] = insurance['smoker'] == 'yes'
predictor = ['age', 'bmi', 'is_smoker']

#splitting into x & y
x = insurance[predictor]
y = insurance['log_charges']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 1)

insurance_model = LinearRegression()
insurance_model.fit(x_train,y_train)
y_pred_test = insurance_model.predict(x_test)

r2_score(y_test,y_pred_test)


st.title('Medical Insurance Prediction Model')
input_text = st.text_input("Enter person's all features")
input_text_splitted = input_text.split(",")
try:
     np_df = np.asarray(input_text_splitted, dtype = float)
     prediction = insurance_model.predict(np_df.reshape(1,-1))
     st.write(f'Medical insurance for this person is {prediction}')
except ValueError:
    st.write("Please Enter numeric value")                       
                           
