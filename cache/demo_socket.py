import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = '10.10.10.44'

# 设置端口号
port = 8090

# 连接服务，指定主机和端口
s.connect((host, port))
ctl = "LIT3" 
s.send(ctl.encode('utf-8'))
# 接收小于 1024 字节的数
sta = s.recv(1024)

s.close()

print (sta.decode('utf-8'))