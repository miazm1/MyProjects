from flask import Flask, request, jsonify
import pickle
import pandas as pd

# init
app = Flask(__name__)

# open model
def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    return model

model_satisfaction = open_model("model.pkl")

def model_inference(data, model=model_satisfaction):
    """
    input : list with length 24 --> ['Inflight wifi service','Online boarding', 'Inflight entertainment', 'Flight Distance', 'On-board service', 'Leg room service','Class','Type of Travel','Customer Type']
    output : predicted class : (idx, label)
    """
    LABEL = ['Neutral/Dissatisfied','Satisfied']
    columns_name = ['Unnamed: 0', 'id', 'Gender', 'Customer Type', 'Age', 'Type of Travel',
       'Class', 'Flight Distance', 'Inflight wifi service',
       'Departure/Arrival time convenient', 'Ease of Online booking',
       'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
       'Inflight entertainment', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Inflight service',
       'Cleanliness', 'Departure Delay in Minutes',
       'Arrival Delay in Minutes']
    data = pd.DataFrame([data], columns=columns_name)
    res = model.predict(data)
    return res[0], LABEL[res[0]]

@app.route("/")
def home():
    return "<h1>Model Works!</h1>"


@app.route("/satisfaction")
def model_predict():
    args = request.args

    unnamed = args.get('Unnamed: 0', type= int, default=0)
    id_number = args.get('id', type= int, default=0)
    gender = args.get('Gender', type= str, default='Female')
    customer_type = args.get('Customer Type', type= str, default='Loyal Customer')
    age = args.get('Age', type= int, default= 0)
    type_of_travel = args.get('Type of Travel',type= str, default='Business travel')
    Class = args.get('Class',type= str, default='Business')
    flight_distance = args.get('Flight Distance',type= int, default=0)
    inflight_wifi_service = args.get('Inflight wifi service',type= int, default=0)
    departure_arrival = args.get('Departure/Arrival time convenient',type= int, default=0)
    online_booking = args.get('Ease of Online booking',type= int, default=0)
    gate_location = args.get('Gate location',type= int, default=0)
    food_drink = args.get('Food and drink',type= int, default=0)
    online_boarding = args.get('Online boarding',type= int, default=0)
    seat_comfort = args.get('Seat comfort',type= int, default=0)
    inflight_entertainment = args.get('Inflight entertainment',type= int, default=0)
    onboard = args.get('On-board service',type= int, default=0)
    leg_room = args.get('Leg room service',type= int, default=0)
    baggage = args.get('Baggage handling',type= int, default=0)
    checkin = args.get('Checkin service',type= int, default=0)
    inflight_service = args.get('Inflight service',type= int, default=0)
    cleanliness = args.get('Cleanliness',type= int, default=0)
    deparature_delay = args.get('Departure Delay in Minutes',type= int, default=0)
    arrival_delay = args.get('Arrival Delay in Minutes',type= float, default=0)

    new_data = [unnamed,id_number,gender,customer_type,age,type_of_travel,Class,
                flight_distance,inflight_wifi_service,departure_arrival,
                online_booking,gate_location,food_drink,online_boarding,
                seat_comfort,inflight_entertainment,onboard,leg_room,
                baggage,checkin,inflight_service,cleanliness,
                deparature_delay,arrival_delay]
    idx, label = model_inference(new_data)
    response = jsonify(result=str(idx), label_names=label)
    return response

# test kode di local
# jika ingin deploy heroku, comment kode dibawah
#app.run(debug=True)