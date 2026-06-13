import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# load dataset
df = pd.read_csv("crop_data.csv")


# features
X = df[
    [
        "nitrogen",
        "phosphorus",
        "potassium",
        "temperature",
        "humidity",
        "rainfall",
        "area",
        "workers"
    ]
]

# target
y = df["crop"]


# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)


# accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


# save model
joblib.dump(model, "model.pkl")


print("Model Saved Successfully!")