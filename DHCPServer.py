import socket
sock67=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock67.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock67.bind(("127.0.0.1", 67))

data, addr = sock67.recvfrom(1024)
print "Received: ", data, " from ", addr
