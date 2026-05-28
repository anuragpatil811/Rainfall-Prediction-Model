import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("rainfall3.pkl", "rb"))
st.title("Rainfall Prediction System")
st.write("Enter weather details below:")
humidity = st.slider("Humidity (%)", 0, 100)
temperature = st.slider("Temperature (°C)", -10, 50)
pressure = st.slider("Pressure (hPa)", 900, 1100)
wind_speed = st.slider("Wind Speed (km/h)", 0, 150)
precipitation = st.slider("Precipitation (mm)", 0.0, 500.0)
cloud_cover = st.slider("Cloud Cover (%)", 0, 100)
input_data = np.array([[humidity,
                        temperature,
                        pressure,
                        wind_speed,
                        precipitation,
                        cloud_cover]])
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("🌧 Rainfall Expected")
    else:
        st.error("☀ No Rainfall Expected")