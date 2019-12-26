import socket
from datetime import datetime

HOST = '192.168.1.64'
PORT = 6789
max_tam = 1024

print('Empezando el cliente en: ', datetime.now())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

while True:
    mensajeAlServidor = input('Escribe algo...')
    mensajeAlServidorEncoded = mensajeAlServidor.encode('utf-8')
    sock.send(mensajeAlServidorEncoded)

    if mensajeAlServidor == 'q':
        break
    
    datos = sock.recv(max_tam)

    if datos.decode('utf-8') == 'q':
        break

    print('A las ', datetime.now(), ' el servidor respondió ', datos.decode('utf-8'))

sock.close()