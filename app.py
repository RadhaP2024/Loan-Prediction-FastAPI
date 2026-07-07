from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import joblib

app = FastAPI()
try:
    model = joblib.load("loan_model.joblib")
except Exception:
    model = None
class LoanRequest(BaseModel):
    Age:int=Field(...,gt=18,lt=100)
    Income_annum:int=Field(...,gt=0,lt=1000000)
    Loan_amount:int=Field(...,gt=0,lt=1000000)
    Cibil:int=Field(...,gt=300,lt=901)
    Property_Area:int=Field(...,gt=0,lt=3)

@app.get("/")
def home():
    return {"message": "Loan Prediction API is Running"}

@app.get("/health")
def health():
    if model is None:
        return{
            "status":"Unhealthy",
            "model":"Not Loaded"
        }
    return{
        "status":"Healthy",
        "model":"Loaded"
    }
    
@app.post("/predict")
def predict(data:LoanRequest):
    if model is None:
        raise HTTPException(status_code=500,detail="Prediction model is not available")
    
    if data.Salary>1000000:
        raise HTTPException(status_code=400,detail="Salary seems unrealistic")
    
    try:
        input_data = [[data.age, data.salary]]
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            result="Loan Approved"
        else:
            result="Loan Rejected"
        return{
            "prediction":result
        }
    except Exception:
        raise HTTPException(status_code=501,detail="Unable to generate prediction")

    result = "Loan Approved" if prediction[0] == 1 else "Loan Rejected"
    return("prediction",result)
