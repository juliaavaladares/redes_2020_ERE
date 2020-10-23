'''

Código Relativo ao Exercício 1:

Cliente UDP recebe 3 entradas: numero 1, numero 2 e a operacao a ser realizada
entre esses dois numeros.
Depois, concatena essas entradas em uma unica string, codifica e manda para o servidor.
Como resposta, ele recebe o resultado da operacao informada.
'''


##Importando bibliotecas

from socket import *

##UDP Cliente

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)

#Usuario deve informar os numeros e a operacao.
n1 = input('Digite um numero: ')
n2 = input('Digite outro nimero: ')
operation = input('Digite a operação a ser feita: ')

#Concatenacao da string
message = n1 + operation + n2
#Envio da e=mensagem para o servidor
clientSocket.sendto(message.encode(), (serverName, serverPort))
#Recebimento da mensagem do Servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()