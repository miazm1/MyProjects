import json
import pandas as pd
import pickle
import streamlit as st
import requests

# load pipeline
pipe = pickle.load(open("model/preprocess_churn.pkl", "rb"))

st.title("Aplikasi Pengecekan Customer Churn")
total_charges = st.number_input("Total Charges",min_value=0)
contract = st.selectbox("Contract", ['Month-to-month','One year','Two year'])
payment_method = st.selectbox("Payment Method", ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check',
 'Mailed check'])
internetservice = st.selectbox("Internet Service", ['DSL','Fiber optic','No'])
onlinesecurity = st.selectbox("Online Security", ['No','No internet service','Yes'])

new_data = {'TotalCharges': total_charges,
         'Contract': contract,
         'PaymentMethod' : payment_method,
         'InternetService' :internetservice,
         'OnlineSecurity' : onlinesecurity}
new_data = pd.DataFrame([new_data])

# build feature
new_data = pipe.transform(new_data)
new_data = new_data.tolist()

# inference
URL = "http://tfserving-azmi.herokuapp.com/v1/models/churn_model:predict"
param = json.dumps({
        "signature_name":"serving_default",
        "instances":new_data
    })
r = requests.post(URL, data=param)

if r.status_code == 200:
    res = r.json()
    if res['predictions'][0][0] > 0.5:
        st.title("Yes")
    else:
        st.title("No")
else:
    st.title("Unexpected Error")