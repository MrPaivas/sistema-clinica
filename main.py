from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pyttsx3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
engine = pyttsx3.init()
consulta_1 = []
consulta_2 = []
lista = []


def texto_p_audio(texto):
    mensagem = "Nova Consulta!"
    lista.append(mensagem)
    lista.append(texto)
    os.remove('./static/audio/audio.mp3')
    engine.setProperty("voice", 0)
    engine.setProperty("gender", "male")
    engine.setProperty("rate", 200)
    engine.save_to_file(lista, './static/audio/audio.mp3')
    engine.runAndWait()
    lista.clear()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/resultado', methods=['GET', 'POST'])
def resultado():
    return render_template('resultado.html')


@socketio.on('conexao')
def on_connect(data):
    print(data)


@socketio.on('message')
def recebe_consulta_velha_2():
    if len(consulta_2) > 1:
        data = consulta_2[-2]
        emit('consulta_velha_2', data, broadcast=True)


@socketio.on('message')
def recebe_consulta_velha():
    if len(consulta_1) > 1:
        data = consulta_1[-2]
        consulta_2.append(data)
        emit('consulta_velha', data, broadcast=True)


@socketio.on('envia_form')
def handle_form_submission(dados):
    consulta_1.append(dados)
    recebe_consulta_velha()
    recebe_consulta_velha_2()
    texto_p_audio(dados)
    emit('atualizar_resultado', dados, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True, host='10.151.22.134', port= 5000)