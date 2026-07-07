from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("loan_model.joblib")

class LoanRequest(BaseModel):
    age: int
    salary: float

@app.get("/")
def home():
    return {"message": "Loan Prediction API is Running"}

@app.post("/predict")
def predict(data: LoanRequest):
    input_data = [[data.age, data.salary]]
    prediction = model.predict(input_data)

    return {
        "prediction": "Loan Approved" if prediction[0] == 1 else "Loan Rejected"
    }