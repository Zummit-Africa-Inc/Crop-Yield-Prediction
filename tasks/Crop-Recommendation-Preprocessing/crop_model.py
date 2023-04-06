import uvicorn
import pickle
from fastapi import FastAPI
from crop_main import Features
import pandas as pd
import numpy as np
import lightgbm as lgb


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


app = FastAPI()
pickle_model = open("CRM.pkl", "rb")
model = pickle.load(pickle_model)


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
    N               = data['N']
    P               = data['P']
    K               = data['K']
    Temperature     = data['Temperature']
    Humidity        = data['Humidity'] 
    PH              = data['PH']
    Rainfall        = data['Rainfall']
    

    Crop_Prediction = model.predict([[N, P, K, Temperature, Humidity, PH, Rainfall]])
    
    return {"This Crop Type is {}".format(Crop_Prediction)}

@app.exception_handler(ValueError)
def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code= 500,
        content={"message": str(exc)},
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)