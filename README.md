# Loan Prediction API using Machine Learning and FastAPI

## 📌 Project Overview

This project is a **Loan Prediction API** built using **Machine Learning** and **FastAPI**. It predicts whether a loan application is likely to be **Approved** or **Rejected** based on two input features:

* Age
* Salary

A **Random Forest Classifier** is trained on historical loan data and exposed through a REST API using FastAPI.

---

## 🚀 Features

* Train a Machine Learning model using Scikit-learn.
* Save the trained model using Joblib.
* Build a REST API with FastAPI.
* Accept loan details as JSON input.
* Predict loan approval status in real time.
* Interactive API documentation with Swagger UI.

---

## 🛠️ Technologies Used

* Python 3.x
* FastAPI
* Scikit-learn
* Pandas
* Joblib
* Uvicorn
* Pydantic

---

## 📁 Project Structure

```text
Loan-Prediction-FastAPI/
│
├── app.py                 # FastAPI application
├── train_model.py         # Model training script
├── data.csv               # Loan dataset
├── model.pkl              # Trained machine learning model
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore
```

---

## 📊 Dataset

The dataset contains the following columns:

| Feature  | Description                              |
| -------- | ---------------------------------------- |
| age      | Applicant's age                          |
| salary   | Applicant's annual salary                |
| approved | Loan status (0 = Rejected, 1 = Approved) |

---

## 🤖 Machine Learning Model

**Algorithm Used:**

* Random Forest Classifier

### Training Steps

1. Load the dataset using Pandas.
2. Select Age and Salary as input features.
3. Use Approved as the target variable.
4. Train the Random Forest model.
5. Save the trained model using Joblib.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Loan-Prediction-FastAPI.git
```

Move into the project folder:

```bash
cd Loan-Prediction-FastAPI
```

Create a virtual environment (optional but recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```bash
python train_model.py
```

This generates:

```text
model.pkl
```

---

## ▶️ Run the FastAPI Server

Start the server with:

```bash
uvicorn app:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 🔗 API Endpoints

### Home Endpoint

**GET /**

Response:

```json
{
  "message": "Loan Prediction API is Running"
}
```

---

### Prediction Endpoint

**POST /predict**

Request Body:

```json
{
  "age": 30,
  "salary": 45000
}
```

Response (Approved):

```json
{
  "prediction": "Loan Approved"
}
```

Response (Rejected):

```json
{
  "prediction": "Loan Rejected"
}
```

---

## 🧪 Example Test

Input:

```json
{
  "age": 24,
  "salary": 32000
}
```

Output:

```json
{
  "prediction": "Loan Rejected"
}
```

Input:

```json
{
  "age": 40,
  "salary": 70000
}
```

Output:

```json
{
  "prediction": "Loan Approved"
}
```

---

## 📈 Future Improvements

* Add more loan eligibility features (credit score, employment status, loan amount, etc.).
* Connect to a database for persistent storage.
* Deploy the API using Docker and cloud platforms.
* Add authentication and authorization.
* Improve model accuracy with additional data and feature engineering.

---

## 📄 License

This project is intended for learning and educational purposes.
