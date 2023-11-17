from flask import Blueprint, render_template

from untils.get_local_ip import link

route_results = Blueprint("resultado", __name__)

@route_results.route('/resultado', methods=['GET', 'POST'])
def resultado():
    return render_template('resultado.html', link=link)