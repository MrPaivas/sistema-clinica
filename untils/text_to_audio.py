import requests
from dotenv import load_dotenv
import os

load_dotenv()
tts_api = os.environ.get('TTP_API_URL')


def texto_p_audio(texto):
    """ Cria um arquivo de audio transquito da mensagem recebida!"""
    params = {"text": texto}
    result = requests.post(url=str(tts_api), params=params)
    return result.text
