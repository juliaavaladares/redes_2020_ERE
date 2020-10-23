'''

Código Relativo ao Exercício 2:

Cliente TCP recebe 3 entradas: numero 1, numero 2 e a operacao a ser realizada
entre esses dois numeros.
Depois, concatena essas entradas em uma unica string, codifica e manda para o servidor.
Como resposta, ele recebe o resultado da operacao informada.
'''



#Biblioteca necessaria
from socket import *

serverName = 'localhost'
serverPort = 3030

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


#Usuario deve informar os numeros e a operacao.
n1 = input('Digite um numero: ')
n2 = input('Digite outro nimero: ')
operation = input('Digite a operação a ser feita: ')

#Concatenacao da string
message = n1 + operation + n2

clientSocket.send(message.encode())
modifiedSentence = clientSocket.recv(1024)

print ('From Server:', modifiedSentence.decode())

clientSocket.close()