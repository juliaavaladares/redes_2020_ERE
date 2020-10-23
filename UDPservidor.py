'''
Código Relativo ao Exercício 1:

Servidor UDP recebe a mensagem enviada pelo cliente no formato (numero operacao numero), exemplo '2+2'.
Com esse formato ele consegue usar o método eval() do Python, que retorna o resultado da operacao desejada
Apos calculada a operacao, o servidor codifica e manda o resultado final para oo cliente.
'''


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