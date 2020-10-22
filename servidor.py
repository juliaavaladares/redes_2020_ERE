##Importando bibliotecas

from socket import *

##UDP Servidor

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('' , serverPort))
print ('The server is ready to receive')
while True:
    print('Waiting...')
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)

    print ('closing socket...')
    serverSocket.close()