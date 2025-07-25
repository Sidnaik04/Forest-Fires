import pickle
from fastapi import FastAPI
from schemas import FirePredictionInput
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Load models
ridge_model = pickle.load(open("models/ridge.pkl", "rb"))
scaler_model = pickle.load(open("models/scaler.pkl", "rb"))

# CORS for frontend access (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return {"message": "Welcome to home page"}


@app.post("/predict")
def predict_fire(input_data: FirePredictionInput):
    columns = [
        "Temperature",
        "RH",
        "Ws",
        "Rain",
        "FFMC",
        "DMC",
        "ISI",
        "Classes",
        "Region",
    ]
    data = pd.DataFrame(
        [
            [
                input_data.Temperature,
                input_data.RH,
                input_data.Ws,
                input_data.Rain,
                input_data.FFMC,
                input_data.DMC,
                input_data.ISI,
                input_data.Classes,
                input_data.Region,
            ]
        ],
        columns=columns,
    )
    scaled = scaler_model.transform(data)
    prediction = ridge_model.predict(scaled)
    return {"prediction": float(prediction[0])}
