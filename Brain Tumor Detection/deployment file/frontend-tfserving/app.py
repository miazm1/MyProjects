import json
import numpy as np
import streamlit as st
import requests
from PIL import Image


st.title("Aplikasi Deteksi Brain Tumor")

uploaded_image = st.file_uploader("Upload CT Scan Image",type=['jpg'])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image)
data_prediction =[]
if st.button('Run Prediction'):
    uploaded_files = Image.open(uploaded_image).resize((180,180))
    uploaded_files = np.array(uploaded_files)
    data           = uploaded_files[np.newaxis,...]
    data_prediction = data.tolist()


# inference
URL = "http://braintumor-backend.herokuapp.com/v1/models/model_brain_cancer_sel:predict"
param = json.dumps({
    "signature_name":"serving_default",
    "instances":data_prediction
})
r = requests.post(URL, data=param)

if r.status_code == 200:
    res = r.json()
    if res['predictions'][0][0] > 0.5:
        st.title("Healthy")
    else:
        st.title("Brain Tumor Detected")
else:
    st.title("No Image or No Prediction")