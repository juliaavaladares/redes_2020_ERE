##Importando bibliotecas

from socket import *

##UDP Cliente

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

n1 = input('Digite um numero: ')
n2 = input('Digite outro nimero: ')
operation = input('Digite a operação a ser feita: ')

message = n1 + operation + n2
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print (modifiedMessage.decode())
clientSocket.close()