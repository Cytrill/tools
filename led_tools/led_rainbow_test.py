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

host = sys.argv[1];
port = 1337;

h = 0

while True:
    h = (h + 1) % 360
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, 1, 1.0)

    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    msg = bytes([ 0x20, r, g, b, 0xFF, 0x20 ])
    s.sendto(msg, (host, port))

    msg = bytes([ 0x21, r, g, b, 0xFF, 0x21 ])
    s.sendto(msg, (host, port))

    time.sleep(0.02)
