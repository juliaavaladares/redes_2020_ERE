'''
Código Relativo ao Exercício 2:

Servidor TCP recebe a mensagem enviada pelo cliente no formato (numero operacao numero), exemplo '2+2'.
Com esse formato ele consegue usar o método eval() do Python, que retorna o resultado da operacao desejada
Apos calculada a operacao, o servidor codifica e manda o resultado final para oo cliente.
'''


#Biblioteca necessaria
from socket import *

serverPort = 3030
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print ('Servidor pronto para receber')


while True:
    connectionSocket, addr = serverSocket.accept()

    message = connectionSocket.recv(1024).decode()
    modifiedMessage = str(eval(message))
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()