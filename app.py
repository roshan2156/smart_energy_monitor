from flask import Flask, render_template, request
from energy_model import predict_energy
from lstm_utils import forecast_energy
import numpy as np
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    current = float(request.form["current"])
    temperature = float(request.form["temperature"])
    month = int(request.form["month"])
    day = int(request.form["day"])
    hour = int(request.form["hour"])
    usage = float(request.form["usage"])

    energy, cost, carbon = predict_energy(
        current, temperature, month, day, hour, usage
    )

    return render_template(
        "index.html",
        energy=round(energy,3),
        cost=round(cost,2),
        carbon=round(carbon,2)
    )

@app.route("/forecast")
def forecast():
    return render_template("forecast.html")

@app.route("/forecast_result", methods=["POST"])
def forecast_result():
    values = request.form["history"]
    history = np.array([float(x) for x in values.split(",")]).reshape(-1,1)

    result = forecast_energy(history, 7)

    return render_template("forecast.html", forecast=result.tolist())

# IMPORTANT FOR RENDER PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
