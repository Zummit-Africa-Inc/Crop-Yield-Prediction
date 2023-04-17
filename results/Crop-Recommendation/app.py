import uvicorn
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from fastapi import FastAPI
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

# Define the input data schema
class Features(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float

app = FastAPI()

# Load the trained model
#model = lgb.Booster(model_file='CRM.txt')
model = joblib.load("CRM.pkl")

# Load the scaler
scaler = joblib.load("scaler.pkl")
@app.get("/")
def root():
    return {"Message": "Welcome to a Crop Recommendation API"}

#@app.get("/Welcome")
#def get_name(name: str):
 #   return {"""Hi Welcome {},  
  #  This is a crop recommendation api, input your values to make Your Predictions""".format(name)}

@app.post("/predict") 
def predict(data:Features):
    data = data.dict()
    N               = data['N']
    P               = data['P']
    K               = data['K']
    temperature     = data['temperature']
    humidity        = data['humidity'] 
    ph              = data['ph']
    rainfall        = data['rainfall']
    

     # Scale the input features
    input_features = scaler.transform([[N, P, K, temperature, humidity, ph, rainfall]])
    
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



