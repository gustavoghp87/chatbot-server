import socket
from decouple import config
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import pandas as pd

HOST = '127.0.0.1'
PORT = int(config("PORT"))

bot = ChatBot(
    'MaslaChat',  
    logic_adapters = ['chatterbot.logic.BestMatch']
)

trainer = ListTrainer(bot)
data = pd.read_excel('frases.xlsx')
list = []

for i in data.index:
    try:
        clave = str(data['clave'][i])
        frase = str(data['frase'][i])
        print(i)
        if clave!='nan':
            list.append(clave)
            list.append(clave)
            print(clave)
        list.append(frase)
        list.append(frase)
        print(frase)
    except:
        print("error")

    if i > 60:
        break

trainer.train(list)
print('\n')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.bind((HOST, PORT))
    socket.listen()
    print('Listening...')
    while 1:
        conn, addr = socket.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            request = str(data)[2:-1].strip()
            print("Other:", request)
            response = bot.get_response(request)
            print('MASLACHAT: ', response, '\n')
            # if not data:
            #     print("Break...")
            #     break
            conn.sendall(str(response).encode('utf-8'))
            conn.close()
