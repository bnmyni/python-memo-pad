from socket import  *
## 创建一个udp的套接字，由于udp是没有状态的，不管发送是否成功，程序都不会理会
udpSocket = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 9988)
sendData = '这个一个测试数据'
udpSocket.sendto(sendData.encode(), addr)
udpSocket.close()