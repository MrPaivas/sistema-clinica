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


def texto_p_audio(texto):
    mensagem = "Nova Consulta!"
    lista = []
    lista.append(mensagem)
    lista.append(texto)
    os.remove('./static/audio/audio.mp3')
    engine.setProperty("voice", 0)
    engine.setProperty("gender", "male")
    engine.setProperty("rate", 200)
    engine.save_to_file(lista, './static/audio/audio.mp3')
    engine.runAndWait()


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
    texto_p_audio(dados)
    emit('atualizar_resultado', dados, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)