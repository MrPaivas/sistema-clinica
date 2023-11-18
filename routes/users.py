from flask import Blueprint, make_response, request

from untils.get_local_ip import link
from untils.check_login import precisa_logar
from mongo.crud import create_user, read_domain

route_user = Blueprint("user", __name__)

@route_user.route('/user', methods=["POST"])
def creat_user():
    data_user = request.form
    domain = data_user['domain']
    username = data_user['username']
    password = data_user['password']
    role = data_user['role']
    if read_domain(domain):
        create_user(domain, username, password, role)
        return make_response("User Created",201)
    else:
        return make_response("Domnio inexistente", 404)