import socket
from multiprocessing import  Process

def handlerClient(clientSocket):
    recvData = clientSocket.recv(2024)
    requestHandlerLines = recvData.splitlines()
    for line in requestHandlerLines:
        print(line)

    responseHeaderLines = 'HTTP/1.1 200 OK\r\n'
    responseHeaderLines += '\r\n'
    responseBody = 'hello,girls'
    response = responseHeaderLines + responseBody
    clientSocket.send(response.encode())
    clientSocket.close()

def main():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(("127.0.0.1", 7788))
    serverSocket.listen(10)
    while True:
        clientSocket, clientAddr = serverSocket.accept()
        clientP = Process(target = handlerClient, args=(clientSocket,))
        clientP.start()
        clientSocket.close()

if __name__ == '__main__':
    main()