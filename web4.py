import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("rainfall4.pkl")

model = load_model()

st.title("🌧️ Advanced Rainfall Prediction System")
st.markdown("### Predict **Annual Rainfall**")

st.sidebar.header("Enter Monthly Rainfall (mm)")

jan = st.sidebar.number_input("January", value=20.0, format="%.2f")
feb = st.sidebar.number_input("February", value=15.0, format="%.2f")
mar = st.sidebar.number_input("March", value=25.0, format="%.2f")
apr = st.sidebar.number_input("April", value=40.0, format="%.2f")
may = st.sidebar.number_input("May", value=80.0, format="%.2f")
jun = st.sidebar.number_input("June", value=150.0, format="%.2f")
jul = st.sidebar.number_input("July", value=280.0, format="%.2f")
aug = st.sidebar.number_input("August", value=260.0, format="%.2f")
sep = st.sidebar.number_input("September", value=180.0, format="%.2f")
octo = st.sidebar.number_input("October", value=80.0, format="%.2f")
nov = st.sidebar.number_input("November", value=30.0, format="%.2f")
dec = st.sidebar.number_input("December", value=15.0, format="%.2f")

if st.sidebar.button("🔮 Predict Annual Rainfall"):
    input_data = pd.DataFrame({
        'JAN': [jan], 'FEB': [feb], 'MAR': [mar], 'APR': [apr],
        'MAY': [may], 'JUN': [jun], 'JUL': [jul], 'AUG': [aug],
        'SEP': [sep], 'OCT': [octo], 'NOV': [nov], 'DEC': [dec]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"**Predicted Annual Rainfall: {prediction:.2f} mm**")

    st.subheader("📊 Monthly Input Summary")
    monthly = pd.DataFrame({
        'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        'Rainfall (mm)': [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec]
    })
    st.table(monthly)

    st.caption("✅ Model Test R² Score: **~0.98** (without district)")