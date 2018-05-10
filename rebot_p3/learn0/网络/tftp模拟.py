from socket import *
import struct
import sys
if len(sys.argv) != 2:
    print('-' * 30)
    print("tips:")
    print("python xxxx.py 192.168.1.1")
    print('-' * 30)
    exit()
else:
    ip = sys.argv[1]

udpSocket = socket(AF_INET, SOCK_DGRAM)
cmd_buf = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)
sendAddr = (ip, 69)
udpSocket.sendto(cmd_buf, sendAddr)

p_num = 0
recv_file = ''

while True:
    recv_data, recv_addr = udpSocket.recv(1024)
    recvDataLen = len(recv_data)
    cmdTuple = struct.unpack("!HH", recv_data[:4])
    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]

    if cmd == 3:
        if currentPackNum == 1:
            recvFile = open("test.jpg", "a")
        if p_num + 1 == currentPackNum:
            recvFile.write(recv_data[4:]);
            p_num += 1
            print('(%d)次接收到的数据' % (p_num))
            ackBuf = struct.pack("!HH", 4, p_num)
            udpSocket.sendto(ackBuf, recv_addr)
        if recvDataLen < 516:
            recvFile.close()
        print( '已经成功下载！！！')
        break
    elif cmd == 5: #是否为错误应答
        print("error num:%d"%currentPackNum)
        break
udpSocket.close()