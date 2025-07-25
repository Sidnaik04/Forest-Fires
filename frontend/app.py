import streamlit as st
import requests

st.title("🔥 Forest Fire Area Prediction")

st.markdown("Enter the environmental parameters below:")

Temperature = st.number_input("Temperature")
RH = st.number_input("Relative Humidity (RH)")
Ws = st.number_input("Wind Speed (Ws)")
Rain = st.number_input("Rainfall (Rain)")
FFMC = st.number_input("FFMC Index")
DMC = st.number_input("DMC Index")
ISI = st.number_input("ISI Index")
Classes = st.selectbox("Classes", [1.0, 2.0])
Region = st.selectbox("Region", [1.0, 2.0])

if st.button("Predict Area Burned"):
    input_data = {
        "Temperature": Temperature,
        "RH": RH,
        "Ws": Ws,
        "Rain": Rain,
        "FFMC": FFMC,
        "DMC": DMC,
        "ISI": ISI,
        "Classes": Classes,
        "Region": Region,
    }
    response = requests.post("http://localhost:8000/predict", json=input_data)
    if response.status_code == 200:
        result = response.json()["prediction"]
        st.success(f"🔥 Predicted area burned: {result:.2f} ha")
    else:
        st.error("Prediction failed. Try again.")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
