#! /usr/bin/end python

import socket

host = "mercury.picoctf.net"
port = 22342

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    # s.sendall(b'Hello, world')
    data = s.recv(1024)

data = str(data)[2:-1].split(' \\n')

flag = ""

for i in range(len(data)):
	if data[i]:
		# print(data[i])
		flag += chr(int(data[i]))


# print(repr(data))
# print(data)
print(flag.strip())