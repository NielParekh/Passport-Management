from flask import Flask, redirect, url_for, render_template, request
from police_login import *
from admin_login import *
from user_register import *
from find_user import *
from police_verify import *
from admin_verify import *
from user_login import *
from check_status import *

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
        if login_status_police[1] == 0:
            return redirect(url_for("police_user_search"))
        else:
            return "invalid"


user_details_police = []


@app.route("/police_user_search", methods=["POST", "GET"])
def police_user_search():
    if request.method == "GET":
        return render_template("police_user_search.html")
        user_details_police.clear()
    else:
        user_id_user = request.form.get('user_id')
        user_exists = find_user(user_id_user)
        user_details_police.append(user_exists)
        if user_exists[1] == 0:
            return redirect(url_for("police_verify"))
        else:
            return "user does not exist"


@app.route("/police_verify", methods=["POST", "GET"])
def police_verify():
    if request.method == "GET":
        return render_template("user_details_display_police.html", user_id=user_details_police[0][0][0],
                               username=user_details_police[0][0][2], address=user_details_police[0][0][6],
                               email=user_details_police[0][0][4], aadhar=user_details_police[0][0][5])
    else:
        if request.form.get('submit_button') == "yes":
            police_verify_status = police_verify_func(user_details_police[0][0][0])
            return f"{police_verify_status}"
        else:
            return "NO"


@app.route("/admin_login", methods=["POST", "GET"])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_admin = admin_login_func(username, password)
        if login_status_admin[1] == 0:
            return redirect(url_for("admin_user_search"))
        else:
            return "invalid"


user_details_admin = []


@app.route("/admin_user_search", methods=["POST", "GET"])
def admin_user_search():
    if request.method == "GET":
        return render_template("admin_user_search.html")
        user_details_admin.clear()
    else:
        user_id_user = request.form.get('user_id')
        user_exists = find_user(user_id_user)
        user_details_admin.append(user_exists)
        if user_exists[1] == 0:
            return redirect(url_for("admin_verify"))
        else:
            return "user does not exist"


@app.route("/admin_verify", methods=["POST", "GET"])
def admin_verify():
    if request.method == "GET":
        return render_template("user_details_display_admin.html", user_id=user_details_admin[0][0][0],
                               username=user_details_admin[0][0][2], address=user_details_admin[0][0][6],
                               email=user_details_admin[0][0][4], aadhar=user_details_admin[0][0][5])
    else:
        if request.form.get('submit_button') == "yes":
            admin_verify_status = admin_verify_func(user_details_admin[0][0][0])
            return f"{admin_verify_status}"
        else:
            return redirect(url_for("login"))


@app.route("/user_choices", methods=["POST", "GET"])
def user_choices():
    if request.form.get('submit_button') == "register":
        return redirect(url_for("user_registration"))
    elif request.form.get('submit_button') == "check_status":
        return redirect(url_for("user_login"))
    else:
        return render_template("user_options.html")


@app.route("/user_login", methods=["POST", "GET"])
def user_login():
    if request.method == "GET":
        return render_template("user_login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        login_status_user = user_login_func(username, password)
        if login_status_user[1] == 0:
            user_status_details = check_status_func(username, password)
            return render_template("user_status.html", admin_status=user_status_details[0],
                                   police_status=user_status_details[1])
        else:
            return "invalid"


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
