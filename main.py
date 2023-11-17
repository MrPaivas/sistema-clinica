from flask import Flask

from config.config import Config
from routes import route_results, route_home, route_login, route_logout
from untils.get_local_ip import ip
from ws.web_socket import socketio


app = Flask(__name__)
app.config.from_object(Config())
socketio.init_app(app)

app.register_blueprint(route_results)
app.register_blueprint(route_home)
app.register_blueprint(route_login)
app.register_blueprint(route_logout)

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True, host=ip, port= 5000)