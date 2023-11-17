from flask import Blueprint, session, redirect

route_logout = Blueprint("logout", __name__)

@route_logout.route("/logout", )
def logout():
    session.pop("user", None)
    return redirect("/login")