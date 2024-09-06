import streamlit as st
from PIL import Image

st.title("GOLD PRICE MODEL")
img = Image.open('gold img.jpg')
st.image(img,width=600,use_column_width=True)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
gold = pd.read_csv('gld_price_data.csv')


#split into X & Y
x = gold.drop(['Date','GLD'],axis = 1)
y = gold.GLD

#split into training & testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 2)

reg = RandomForestRegressor()
reg.fit(x_train,y_train)
y_pred = reg.predict(x_test)
score = r2_score(y_test,y_pred)

st.subheader('Using randomforestregressor')
st.write(gold)
st.subheader('Model Performance')
st.write(score)
