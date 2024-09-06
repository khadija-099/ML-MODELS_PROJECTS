import numpy as np
import pandas as pd
import pickle
from flask  import Flask,request,render_template


#loading model
model = pickle.load(open('Netflix_model.pkl','rb'))
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    Open  = request.form['Open']
    High = request.form['High']
    Low = request.form['Low']
    Adj_Close= request.form['Adj_Close']
    Volume = request.form['Volume']
    year = request.form['Year']
    month = request.form['Month']
    day  = request.form['Day']

    features = np.array([[Open,High,Low,Adj_Close,Volume,Year,Month,Day]])
    features = scale.fit_transform(features)
    prediction = model.predict(features).reshape(1,-1)

    return render_template('index.html',output = prediction)

#main python
if __name__ == '__main__':
    app.run(debug=True)

