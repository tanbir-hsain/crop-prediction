import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = pd.read_csv("crop_data.csv")

X = data[[
    "nitrogen",
    "phosphorus",
    "potassium",
    "temperature",
    "humidity",
    "rainfall",
    "area",
    "workers"
]]

y = data["crop"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model Saved")