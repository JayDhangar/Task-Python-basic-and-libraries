from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello</h1>
    <form action="/submit" method="POST">
        <input type="text" name="data" placeholder="Enter your name ">
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/submit", methods=["POST"])
def submit():
    value = request.form["data"]
    return f"Welcome: {value}"

if __name__ == "__main__":
    app.run(debug=True)