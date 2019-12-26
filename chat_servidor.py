import socket
from datetime import datetime

HOST = '192.168.1.64'
PORT = 6789
max_tam = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

print('Empezando el servidor en: ', datetime.now())
print('Esperando conexión...')

sock.listen(5)
cliente, direccion = sock.accept()

while True:
    datos = cliente.recv(max_tam)
    if datos.decode('utf-8') == 'q':
        break

    print('A las ', datetime.now(), direccion, ' dijo', datos.decode('utf-8'))
    mensajeAlCliente = input('Escribe algo...')
    mensajeAlClienteEncoded = mensajeAlCliente.encode('utf-8')
    cliente.send(mensajeAlClienteEncoded)

    if mensajeAlCliente == 'q':
        break

cliente.close()
sock.close()