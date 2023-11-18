from flask import Blueprint, jsonify, make_response

from untils.get_local_ip import link
from untils.check_login import precisa_logar
from mongo.crud import create_domain

route_domain = Blueprint("domain", __name__)

@route_domain.route('/domain/<string:name>/<string:cnpj>', methods=["POST"])
def domain(name, cnpj):
    response = create_domain(name, cnpj)
    response['_id'] = str(response['_id']) if '_id' in response else None
    return make_response(jsonify(response), 201)