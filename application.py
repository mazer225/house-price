import uvicorn
from fastapi import FastAPI
from Price import Cost
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("House_Price_Pred.pkl", "rb")
Prediction = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.post('/predict')
def predict_house_price(data: Cost):
    # print("hello")
    print(data)
    data = data.dict()
    area = data['area']
    bedrooms = data['bedrooms']
    bathrooms = data['bathrooms']
    stories = data['stories']
    parking = data['parking']
    furnishingstatus = data['furnishingstatus']
    if(furnishingstatus == "furnished"):
        furstatus = 0
    elif(furnishingstatus == "semi-furnished"):
        furstatus = 1
    else:
        furstatus = 2
    print(Prediction.predict(
        [[area, bedrooms, bathrooms, stories, parking, furstatus]]))
    result = Prediction.predict(
        [[area, bedrooms, bathrooms, stories, parking, furstatus]])
    if(result[0] > 1500000):
        prediction = "High"
    else:
        prediction = "low"
    return {
        'prediction': prediction
    }


#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn application:app --reload
