
import streamlit as st

st.title("Credit Card Fraud Detection Model")
input_df = st.text_input('Enter All Required Features Values')
input_df_splitted = input_df.split(',')

submit = st.button('Submit')
if submit:
    features = np.asarray(input_df_splitted,dtype = np.float64)
    prediction = model.predict(features.reshape(-1,1))

    if prediction == 0:
        st.write('Legitimate Transaction')

    else:
        st.write('Fraudulent Transaction')
