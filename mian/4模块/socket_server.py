import socket

sk = socket.socket()

# 绑定端口号
sk.bind(('127.0.0.1', 8081))

sk.listen(5)

# 等待连接
conn, addr = sk.accept()
print(conn)
print(addr)

while True:
    # 收到客户端消息
    print(conn.recv(1024).decode("utf-8"))

    conn.send("收到".encode("utf-8"))