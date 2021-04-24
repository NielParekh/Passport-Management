from flask import Flask, redirect, url_for, render_template, request
from police_login import *
from admin_login import *
from user_register import *

app = Flask(__name__)


@app.route("/")
def hello():
    exec(open('setup.py').read())
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.form.get('submit_button') == "police":
        return redirect(url_for("police_login"))
    elif request.form.get('submit_button') == "admin":
        return redirect(url_for("admin_login"))
    elif request.form.get('submit_button') == "user":
        return redirect(url_for("user_choices"))
    else:
        return render_template("index.html")


@app.route("/police_login", methods=["POST", "GET"])
def police_login():
    if request.method == "GET":
        return render_template("police_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_police = police_login_func(username, password)
        return f"{login_status_police[0]}"


@app.route("/admin_login", methods=["POST", "GET"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_admin = admin_login_func(username, password)
        return f"{login_status_admin[0]}"


@app.route("/user_choices", methods=["POST", "GET"])
def user_choices():
    if request.form.get('submit_button') == "register":
        return redirect(url_for("user_registration"))
    elif request.form.get('submit_button') == "check_status":
        return "<h1>O<\h1>"
    else:
        return render_template("user_options.html")


@app.route("/user_registration", methods=["POST", "GET"])
def user_registration():
    if request.method == "GET":
        return render_template("user_registration.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        aadhar = request.form.get("aadhar")
        address = request.form.get("address")
        choice = request.form.get("reg")
        registration_status_user = user_register(username, password, email, aadhar, address, choice)
        return f"{registration_status_user}"


if __name__ == "__main__":
    app.run(debug=True)
