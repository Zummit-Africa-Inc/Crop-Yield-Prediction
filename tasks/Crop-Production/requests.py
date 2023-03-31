import requests

input_data = [{"District_Name": 'YADGIR', 
               "Crop_Year": 2011,        
               "Season": 'Rabi',        
               "Crop": 'Groundnut',       
               "Area": 23194.0 }]

response = requests.post("http://localhost:8000/predict", json=input_data)

if response.status_code in range(200, 300):
    data = response.json()
    print(data)
else:
    print("Error: status code", response.status_code)