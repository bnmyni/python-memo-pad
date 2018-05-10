import socket
from multiprocessing import Process
import re


def hanleClient(clientSocket):
    ## parse request
    recvData = clientSocket.recv(2024)
    requestHeaderLines = recvData.splitlines()
    for line in requestHeaderLines:
        print(line)

    ## response
    httpRequestMethodLine = requestHeaderLines[0]
    ## 匹配一个已非/开头并且后面带有/word的字符
    getFileName = re.match("[^/]+(/[^ ]*)", httpRequestMethodLine.decode()).group(1)
    if getFileName == '/':
        getFileName = documentRoot + '/index.html'
    else:
        getFileName = documentRoot + getFileName

    try:
        f = open(getFileName, 'r', encoding='utf-8')
    except:
        responseHeaderLines = 'HTTP/1.1 404 OK\r\n'
        responseHeaderLines += '\r\n'
        responseBody = 'sorry, file not found'
    else:
        responseHeaderLines = 'HTTP/1.1 200 OK\r\n'
        responseHeaderLines += '\r\n'
        responseBody = f.read()
        print('responseBody : %s' % responseBody)
        f.close()
    finally:
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
        clientP = Process(target = hanleClient, args=(clientSocket,))
        clientP.start()
        clientSocket.close()

documentRoot = 'C:\\Users\\sunke\\Desktop'
if __name__ == '__main__':
    main()