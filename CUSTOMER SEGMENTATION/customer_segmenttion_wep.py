
import streamlit as st

st.title("CUSTOMER CLUSTERING APP")
st.write("Enter customer details")

#row1
col1, col2 = st.columns(2)
with col1:
    st.subheader("Customer Age")
    age = st.number_input('Age',min_value=18, max_value=100)
    
with col1:
    st.subheader("Customer Spent Time")
    avg_spend = st.number_input('Average Spend',min_value=0.0, max_value=1000.0)    
    
    
#row2
col1, col2 = st.columns(2)
with col1:
    st.subheader("Visits Per Week")
    visits_per_week = st.number_input('Visits Per Week',min_value=10, max_value=20)
    
with col1:
    st.subheader("Promotion Interest")
    prom_interest = st.number_input('Promotion Interest',min_value=0, max_value=10)   
    


def clustering(age , avg_spend, visit_per_week, promotion_interest):
    new_customer = np.array([[age, avg_spend, visits_per_week, promotion_interest]])
    predicted_cluster = kmeans.predict(new_customer)
    
    if predicted_cluster ==0:
        return "Daily"
    
    elif predicted_cluster ==1:
        return "Promotion"
    
    else:
        return "Weekend"
    

    
    
    if st.button("Predict Cluster"):
        cluster_label= clustering(age , avg_spend, visits_per_week, promotion_interest)
        st.write(f"The customer belongs to {cluster_label} cluster.")
        
    
