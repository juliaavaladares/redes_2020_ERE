##Importando bibliotecas

from socket import *

##UDP Servidor

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('' , serverPort))
print ('Servidor pronto para receber mensagens')

while True:
    print('Esperando inicializacao')
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = str(eval(message.decode()))
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)

    print ('Socket fechado')
    serverSocket.close()