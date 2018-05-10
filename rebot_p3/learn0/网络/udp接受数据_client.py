from socket import *

client = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 9988)
client.bind(addr)
data = client.recv(1024).decode()
print(data)

client.close()