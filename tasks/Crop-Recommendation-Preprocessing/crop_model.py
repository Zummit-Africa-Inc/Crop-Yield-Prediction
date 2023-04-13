import uvicorn
import pickle
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.preprocessing import MinMaxScaler
from fastapi import FastAPI
from crop_main import Features
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Load the trained model
pickle_model = open("CRM.pkl", "rb")
model = pickle.load(pickle_model)

# Load the scaler
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.get("/")
def root():
    return {"Message": "Building a CROP PREDICTION API"}

@app.get("/Welcome")
def get_name(name: str):
    return {"""Hi Welcome {},  
    This is a crop prediction api, input your values to make Your Predictions""".format(name)}

@app.post("/predict") 
def predict(data:Features):
    data = data.dict()
    N = data['N']
    P = data['P']
    K = data['K']
    Temperature = data['Temperature']
    Humidity = data['Humidity'] 
    PH = data['PH']
    Rainfall = data['Rainfall']
    
    # Scale the input features
    input_features = scaler.transform([[N, P, K, Temperature, Humidity, PH, Rainfall]])
    
    # Make the prediction using the scaled input features
    crop_prediction = model.predict(input_features)
    
    return {"This Crop Type is {}".format(crop_prediction)}

@app.exception_handler(ValueError)
def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code= 500,
        content={"message": str(exc)},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
