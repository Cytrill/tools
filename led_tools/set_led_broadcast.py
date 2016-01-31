#!/usr/bin/env python
import sys
import socket
import colorsys
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
except:
    print('Failed to create socket')
    sys.exit(1)

host = sys.argv[1];
port = 1337;

r = int(sys.argv[3])
g = int(sys.argv[4])
b = int(sys.argv[5])

msg = bytes([ 0x20 + int(sys.argv[2]), r, g, b, 0x1F, 0x20 + int(sys.argv[2]) ])
s.sendto(msg, (host, port))
