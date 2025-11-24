from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app=Flask(__name__)

@app.route("/")
def dashboard():

    datafile = pd.read_csv("data.csv")

    numbers = datafile["salary"].fillna(0).to_numpy()
    stats = {
        "sum": int(np.sum(numbers)),
        "mean": float(np.mean(numbers)),
        "max": int(np.max(numbers)),
        "min": int(np.min(numbers))
    }

    plt.figure()
    plt.plot(numbers)
    plt.title("salary Trend")
    plt.xlabel("Index")
    plt.ylabel("Salary")
    plt.savefig("static/dog.png")
    plt.close()

    return render_template("htmlfile.html", stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
