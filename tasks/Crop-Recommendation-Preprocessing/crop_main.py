from pydantic import BaseModel

class Features(BaseModel):
    N:              int 
    P:              int
    K:              int  
    Temperature:    float
    Humidity:       float    
    PH:             float
    Rainfall:       float 

