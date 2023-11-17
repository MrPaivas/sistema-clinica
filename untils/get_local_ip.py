import socket

def coleta_o_ip():
    try:
        # Cria um socket UDP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Conecta-se a um servidor público qualquer, apenas para obter o endereço IP local
        s.connect(("8.8.8.8", 80))

        # Obtém o endereço IP local
        local_ip = s.getsockname()[0]

        # Fecha o socket
        s.close()
        print(local_ip)
        return local_ip
    except Exception as e:
        print("Ocorreu um erro ao obter o endereço IP local:", e)
        return None
    
ip = coleta_o_ip()
link = 'http://' + str(ip) + ':5000'