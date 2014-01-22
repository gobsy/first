__author__ = 'GobovAY'
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost
import socket
import sys
IP = '85.94.33.20'
#IP = '127.0.0.1'



MAX = 65535
PORT = 9876
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print 'Address before sending:', s.getsockname()
#s.sendto('This is my message', ('127.0.0.1', PORT))
s.sendto('This is my message', ('85.94.33.20', PORT))
#print 'Address after sending', s.getsockname()
data, address = s.recvfrom(MAX) # overly promiscuous - see text!
print 'The server', address, 'says', repr(data)
'''



target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    target.connect((IP, PORT))

    print 'sending:'
    try:
        target.send("test data: 9834573024987532479")
    except:
        print 'can not send '
        target.close()


except:
    print 'error'
    sys.exit()
