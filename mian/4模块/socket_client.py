import socket
sock = socket.socket()

# 连接端口
sock.connect(('127.0.0.1', 8081))

while True:
    s = input("client send:")
    sock.send(str(s).encode("utf-8"))

    print(sock.recv(1024).decode("utf-8"))