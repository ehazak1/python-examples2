import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = raw_input('% ')
        s.sendto(msg, ('128.107.53.56', 9601))
        print s.recvfrom(256)
finally:
    s.close()
        
