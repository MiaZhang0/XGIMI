# -*- coding:utf-8 -*-
import socket
import time

result = socket.getaddrinfo("srm-in.d.xgimi.com", None)
print(result[0][4][0])
# t = time.time()
# print(t)