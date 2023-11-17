from flask import Blueprint, render_template

from untils.get_local_ip import link
from untils.check_login import precisa_logar

route_home = Blueprint("/", __name__)

@route_home.route('/')
@precisa_logar
def home():
    return render_template('home.html', link=link)