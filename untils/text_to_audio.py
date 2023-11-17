import pyttsx3
import os

engine = pyttsx3.init()

def texto_p_audio(texto):
    """ Cria um arquivo de audio transquito da mensagem recebida!"""
    lista=[]
    consulta = texto.copy()
    consulta.pop("toca_som")
    mensagem = "Nova Consulta!"
    lista.append(mensagem)
    lista.append(consulta)
    os.remove('./static/audio/audio.mp3')
    engine.setProperty("voice", 0)
    engine.setProperty("gender", "male")
    engine.setProperty("rate", 200)
    engine.save_to_file(lista, './static/audio/audio.mp3')
    engine.runAndWait()
    lista.clear()