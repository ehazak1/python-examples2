'Show how to make a UDP server'

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9601))
try:
    while True:
        msg, who = s.recvfrom(256)
        print 'Received a call from: %r' % (who,)
        print 'They said: %r' % msg
        s.sendto(time.ctime(), who)
finally:
    s.close()

