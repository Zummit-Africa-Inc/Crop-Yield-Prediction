import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Load the trained model
model = joblib.load("catboost_model.pkl")

# Define the input data schema
class InputData(BaseModel):
    District_Name: str
    Crop_Year: int
    Season: str
    Crop: str
    Area: float

# Define the output data schema
class OutputData(BaseModel):
    Prediction: float

# Create the FastAPI app instance
app = FastAPI()

# Define the API endpoint
@app.post("/predict", response_model=List[OutputData])
async def predict_yield(inputs: List[InputData]):
    predictions = []
    for input_data in inputs:
        # Create a DataFrame from the input data
        input_df = pd.DataFrame([input_data.dict()])
        
        # Make the prediction using the loaded model
        prediction = abs(model.predict(input_df)[0])
        
        # Create an OutputData object with the prediction
        output_data = OutputData(Prediction=prediction)
        
        # Append the output data to the list of predictions
        predictions.append(output_data)
    
    # Return the list of predictions
    return predictions
