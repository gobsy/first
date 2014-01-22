__author__ = 'GobovAY'
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost
import socket
#import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 9876

#if sys.argv[1:] == ['server']:
s.bind(('127.0.0.1', PORT))
print 'Listening at', s.getsockname()
'''
while True:
    data, address = s.recvfrom(MAX)
    print 'The client at', address, 'says', repr(data)
    s.sendto('Your data was %d bytes' % len(data), address)
'''
while 1:
    datagram = s.recv(1024)
    if not datagram:
        break
    print repr(datagram)

s.close()