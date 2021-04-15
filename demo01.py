import socket
host = 'srm.t.xgimi.com'
ip = socket.getaddrinfo(host,None)
print(ip[0][4][0])