from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('Server ready')
while 1:
     connectionSocket, addr = serverSocket.accept()
     print('Connected new client')
     sentence = connectionSocket.recv(1024)
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence)
     print('Reply sent to client ')
     connectionSocket.close()
     print('The connection with the client was terminated')
