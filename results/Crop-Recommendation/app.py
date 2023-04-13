import pandas as pd
import numpy as np
import pickle
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, Request
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
pickle_model = open("CRM.pkl", "rb")
model = pickle.load(pickle_model)

@app.get("/")
def root():
    return {"Message": "Building a CROP PREDICTION API"}

@app.get("/Welcome")
def get_name(name: str):
    return {"""Hi Welcome {},  
    This is a crop recommendation api, input your values to make Your Predictions""".format(name)}

@app.post("/predict") 
def predict(data:Features):
    data = data.dict()
    N               = data['N']
    P               = data['P']
    K               = data['K']
    Temperature     = data['Temperature']
    Humidity        = data['Humidity'] 
    PH              = data['PH']
    Rainfall        = data['Rainfall']
    

    Crop_Prediction = model.predict([[N, P, K, Temperature, Humidity, PH, Rainfall]])
    
    return {"The Crop Recommended is {}".format(Crop_Prediction)}

@app.exception_handler(ValueError)
def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code= 500,
        content={"message": str(exc)},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




