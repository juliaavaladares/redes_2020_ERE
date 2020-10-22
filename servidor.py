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


##UDP Cliente

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),

(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print (modifiedMessage.decode())
clientSocket.close()