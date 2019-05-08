import socket

sock68=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
sock68.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock68.bind(("127.0.0.1", 68))

MESSAGE = "Hello, World!"
sock68.sendto(MESSAGE, ("127.0.0.1", 67))
