from flask import Blueprint, render_template, session, request, redirect

from mongo.crud import check_password


route_login = Blueprint("login", __name__)


@route_login.route('/login')
def login():
    return render_template('login.html')

@route_login.route('/login', methods=["POST"])
def mk_login():
    username = request.form["username"]
    password = request.form["password"]
    if check_password(username, password):
        session["user"] = username
        return redirect("/")
    return render_template('login.html')