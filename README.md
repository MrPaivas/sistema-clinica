#Introdução#

Este é um código Python que utiliza o framework Flask e a extensão Flask-SocketIO para criar um servidor que permite que os usuários enviem consultas por meio de um formulário e recebam uma resposta de volta em tempo real. Além disso, o código utiliza a biblioteca pyttsx3 para converter o texto das consultas em áudio, que é então reproduzido para o usuário.

###Como Instalar###

#1 Instale o Python
  instale a versão mais nova do python em: https://www.python.org/downloads/

#2 Coloque o Python e o PiP(Gerenciador de Pacotes do Python) nas variaveis de ambiente do Windows:
  siga o passo a passo:
    https://www.tekimobile.com/dicas/como-adicionar-python-a-variavel-path-do-windows/

#3 Selecione um IP na sua REDE LOCAL
  siga o passo a passo:
    https://www.youtube.com/watch?v=HoEIA2F2Ivo&ab_channel=CIATecnologiaNews

#4 Baixe esse código.
  1 Clique em <>CODE e depois Download ZIP.
  ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/2cc72853-fd52-462c-bc57-249ef158405e)

  2 Extraia os arquivos onde preferir.

  
  3 Abra o CMD e navegue até a pasta selecionada.
  ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/98c97d70-5fd1-4094-a5a5-1e2c12b30308)

  
  4 Inicie um ambiente virtual do python com o seguinte comando.
  "python -m venv venv"
    ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/2e4e55ee-ed1f-4377-a11e-0f73c2d807c5)
  esse comando vai criar uma pasta chamada venv dentro da pasta do sistema
    ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/52381a83-a801-4a2d-a890-6d3b69cad8c8)
  agora no cmd inicie a VENV com o seguinte comando:
    "venv\Scripts\activate.bat"
    ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/45f993d8-e5a1-4266-bd97-edec7fd3a2fc)
  Note que existe (venv) na linha de comando do CMD


  5 Baixe As bibliotecas necessárias usando o pip e o arquivo requirementes.txt com esse comando:
    "pip install -r requirements.txt"
    ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/aa53e051-fe17-4503-ae44-7908c0192ef6)

  #5 Agora só realizar o ultimo e iniciar o arquivo main.py com o seguinte comando:
    "python main.py"
    ![image](https://github.com/MrPaivas/sistema-clinica/assets/118641977/9d5fd4a0-69f4-42f0-9ce9-d8dd525cb14d)

  #6 Para acessar as paginas é só seguir esse link da ultima foto, no meu caso "http://10.151.22.132:5000" e "http://10.151.22.132:5000/resultado" para tela de resultado.

  ##DICA FINAL 
  #### ALTERAR AS PERMIÇOES DA PAGINA DE RESULTADO PARA PERMITR SONS, SE NÃO, NÃO FUNCIONARÁ SONS EMITIDOS PELO NAVEGADOR QUANDO TEM UMA NOVA CHAMADA


  
