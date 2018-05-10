import socket
'''
Address Family：可以选择 AF_INET（ Internet 进程间通信） 或者 AF_UNIX 同一个机器
Type：套接字类型，可以是 SOCK_STREAM（流式套接字，用于TCP 协议）
或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
'''
## tcp
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sendAddr = ('10.1.3.33', 8080)

data = socket.raw_input('hello:')

udpSocket.sendto(data, sendAddr)
udpSocket.close()

