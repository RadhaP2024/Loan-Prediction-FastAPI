import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data.csv")

X = df[["age", "salary"]]
y = df["approved"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "loan_model.joblib")

print("Model saved successfully!")