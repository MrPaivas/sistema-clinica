from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
consulta_1 = []
consulta_2 = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    return render_template('resultado.html')


@socketio.on('conexao')
def on_connect(data):
    print(data)


@socketio.on('envia_form')
def handle_form_submission(dados):
    consulta_1.append(dados)
    emit('atualizar_resultado', dados, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)