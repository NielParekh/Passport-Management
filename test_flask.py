from flask import Flask, redirect, url_for, render_template, request
from police_login import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "HELLO"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user1 = request.form.get("nm")
        return redirect(url_for("user_display", usr=user1))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user_display(usr):
    return f"HELLO {usr}"


@app.route("/test", methods=["POST", "GET"])
def test():
    if request.form.get('submit_button') == "police":
        temp = police_login()
        return f"{temp}"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
