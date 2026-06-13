from flask import Flask, render_template, request
import joblib


# create flask application
app = Flask(__name__)


# load trained model
model = joblib.load("model.pkl")


# home page
@app.route("/")
def home():
    return render_template("index.html")


# prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():

    # get input values from form
    n = float(request.form["nitrogen"])
    p = float(request.form["phosphorus"])
    k = float(request.form["potassium"])
    t = float(request.form["temperature"])
    h = float(request.form["humidity"])
    r = float(request.form["rainfall"])
    a = float(request.form["area"])
    w = float(request.form["workers"])

    # predict crop using trained model
    crop = model.predict([[n, p, k, t, h, r, a, w]])[0]

    # calculate estimated farming cost
    cost = int(a * 15000)

    # calculate estimated profit
    profit = int(a * 10000)

    # send result back to webpage
    return render_template(
        "index.html",
        crop=crop,
        cost=cost,
        profit=profit
    )


# run flask server
app.run(host="0.0.0.0", port=5000)