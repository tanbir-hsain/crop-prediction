from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    n = float(request.form["nitrogen"])
    p = float(request.form["phosphorus"])
    k = float(request.form["potassium"])
    t = float(request.form["temperature"])
    h = float(request.form["humidity"])
    r = float(request.form["rainfall"])
    a = float(request.form["area"])
    w = float(request.form["workers"])

    crop = model.predict([[n,p,k,t,h,r,a,w]])[0]

    cost = int(a * 15000)
    profit = int(a * 10000)

    return render_template(
        "index.html",
        crop=crop,
        cost=cost,
        profit=profit
    )

app.run(host="0.0.0.0", port=5000)