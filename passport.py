from flask import Flask, redirect, url_for, render_template, request
from police_login import *
from admin_login import *

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form.get('submit_button') == "police":
        login_details = police_login()
        return f"{login_details[0]}"
    elif request.form.get('submit_button') == "admin":
        login_details = admin_login()
        return f"{login_details[0]}"
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
