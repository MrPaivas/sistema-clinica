from flask_socketio import SocketIO, emit
import json

from untils.text_to_audio import texto_p_audio
from untils.text_format import format_text

socketio = SocketIO()

consulta_1 = []
consulta_2 = []

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
    if dados.get('toca_som'):
        text = format_text(dados)
        try:
            b64_audio = texto_p_audio(text)
            dados.update(json.loads(b64_audio))
        except Exception as err:
            print(err)
    emit('atualizar_resultado', dados, broadcast=True)