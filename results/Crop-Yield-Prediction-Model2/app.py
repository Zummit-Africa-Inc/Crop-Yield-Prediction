import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sklearn.preprocessing import MinMaxScaler

# Load the trained model
model = joblib.load("best_model.pkl")

# Define the input data schema 
class InputData(BaseModel):
    Item: str
    average_rain_fall_mm_per_year: float
    pesticides_tonnes: float
    avg_temp: float
    

# Define the output data schema
class OutputData(BaseModel):
    Prediction: float

# Define the cleanup mapping for Item feature
cleanup_nums = {'Item': {'Potatoes':0,
                         'Maize':1, 
                         'Wheat':2, 
                         'Rice, paddy':3,
                         'Soybeans':4,
                         'Sorghum':5,
                         'Sweet potatoes':6, 
                         'Cassava':7, 
                         'Yams':8,
                         'Plantains and others':9}}

# Create the FastAPI app instance
app = FastAPI()

# Define the API endpoint
@app.post("/predict", response_model=List[OutputData])
async def predict_yield(inputs: List[InputData]):
    # Create a DataFrame from the input data
    input_dict = [input_data.dict() for input_data in inputs]
    input_df = pd.DataFrame(input_dict)
    
    # Apply the cleanup mapping for the Item feature
    input_df.replace(cleanup_nums, inplace=True)
    
    # Scale the features using MinMaxScaler
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(input_df), columns=input_df.columns)
    
    # Make the prediction using the loaded model
    predictions = model.predict(scaled_df)
    
    # Create a list of OutputData objects with the predictions
    output_list = [OutputData(Prediction=prediction) for prediction in predictions]
    
    # Return the list of OutputData objects
    return output_list
    
if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)