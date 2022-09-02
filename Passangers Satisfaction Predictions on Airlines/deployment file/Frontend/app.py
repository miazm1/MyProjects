import streamlit as st
import requests

st.title("Satisfaction Passenger")

col1, col2 = st.columns(2)

with col1:
    st.subheader('Customer Information')
    unnamed = 0
    id = st.text_input("ID Customer")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age",step=1)

with col2:
    st.subheader('Flight Information')
    customer_type = st.selectbox("Customer Type", ['Loyal Customer','disloyal Customer'])
    Class = st.selectbox("Class", [ 'Eco','Eco Plus','Business'])
    flight_distance = st.number_input("Flight Distance",step=1)
    deparature_delay = st.number_input("Departure Delay in Minutes",step=1)
    arrival_delay = st.number_input("Arrival Delay in Minutes",step=1)

st.subheader('Service Rating')
inflight_wifi_service = st.selectbox("Inflight Wifi Service Rating", [0,1, 2, 3,4,5])
departure_arrival = st.selectbox("Deparature/Arrival Time Rating", [0,1, 2, 3,4,5])
online_booking = st.selectbox("Online Booking Services Rating", [0,1, 2, 3,4,5])
gate_location = st.selectbox("Gate Location Rating", [0,1, 2, 3,4,5])
food_drink = st.selectbox("Food and Drink Rating", [0,1, 2, 3,4,5])
online_boarding = st.selectbox("Online Boarding Services Rating", [0,1, 2, 3,4,5])
seat_comfort = st.selectbox("Seat Comfort Rating", [0,1, 2, 3,4,5])
inflight_entertainment = st.selectbox("Inflight Entertainment Rating", [0,1, 2, 3,4,5])
onboard = st.selectbox("On-board Services Rating", [0,1, 2, 3,4,5])
leg_room = st.selectbox("Leg Room Rating", [0,1, 2, 3,4,5])
baggage = st.selectbox("Baggage Handling Rating", [0,1, 2, 3,4,5])
checkin = st.selectbox("Check-in Rating", [0,1, 2, 3,4,5])
inflight_service = st.selectbox("Inflight Services Rating", [0,1, 2, 3,4,5])
cleanliness = st.selectbox("Cleanliness Rating", [0,1, 2, 3,4,5])

# inference
URL = "https://model-deployment-satisfaction.herokuapp.com/satisfaction"
param = {'unnamed': unnamed,
         'id_number': id,
         'gender': gender,
         'customer_type': customer_type,
         'age' : age,
         'Class' :Class,
         'flight_distance': flight_distance,
         'inflight_wifi_service': inflight_wifi_service,
         'departure_arrival' : departure_arrival,
         'online_booking' : online_booking,
         'gate_location': gate_location,
         'food_drink': food_drink,
         'online_boarding' : online_boarding,
         'seat_comfort' : seat_comfort,
         'inflight_entertainment' : inflight_entertainment,
         'onboard' : onboard,
         'leg_room': leg_room,
         'baggage': baggage,
         'checkin' : checkin,
         'inflight_service' : inflight_service,
         'cleanliness' : cleanliness,
         'deparature_delay' : deparature_delay,
         'arrival_delay' : arrival_delay}

st.subheader('Customer Satisfaction :')
r = requests.post(URL, json=param)

if r.status_code == 200:
    res = r.json()
    st.title(res['label_names'])
else:
    st.title("Unexpected Error")