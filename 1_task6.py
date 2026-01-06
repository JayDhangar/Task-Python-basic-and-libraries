from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def dashboard():

    datafile = pd.read_csv("data1/data.csv")
    x = datafile["perimeter_worst"]
    y = datafile["area_worst"]

    stats = {
        "perimeter_mean": float(np.mean(x)),
        "area_mean": float(np.mean(y)),
        "perimeter_max": int(np.max(x)),
        "area_max": int(np.max(y))
    }

    os.makedirs("static",exist_ok=True)

    plt.figure()
    plt.scatter(x, y)
    plt.title("Perimeter vs Area ")
    plt.xlabel("Perimeter Worst")
    plt.ylabel("Area Worst")
    plt.savefig("static/dog.png")
    plt.close()

    return render_template("htmlfile.html",stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
