import pickle
import numpy as np

model = pickle.load(open("models/anemia_model.pkl","rb"))
scaler = pickle.load(open("models/scaler.pkl","rb"))

def predict_anemia(input_data):
    scaled = scaler.transform([input_data])
    prediction = model.predict(scaled)
    probability = model.predict_proba(scaled)
    return prediction[0], probability[0][1]
