#!/usr/bin/env python
import sys
import socket
import colorsys
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print('Failed to create socket')
    sys.exit(1)

host = "10.23.42.147";
port = 1337;

r = int(sys.argv[2])
g = int(sys.argv[3])
b = int(sys.argv[4])

msg = bytes([ 0x20 + int(sys.argv[1]), r, g, b, 0x04, 0x20 + int(sys.argv[1]) ])
s.sendto(msg, (host, port))
