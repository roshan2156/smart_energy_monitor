import numpy as np

def forecast_energy(history, days):

    last_value = history[-1][0]
    forecast = []

    for i in range(days):
        next_val = last_value * (1 + np.random.uniform(-0.05, 0.05))
        forecast.append(round(next_val, 2))
        last_value = next_val

    return forecast
