#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: David Manouchehri <manouchehri@protonmail.com>
# This script will always echo back data on the UDP port of your choice.
# Useful if you want nmap to report a UDP port as "open" instead of "open|filtered" on a standard scan.
# Works with both Python 2 & 3.

import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '132.145.58.228'
server_port = 31337

server = (server_address, server_port)

while True:
      sent = sock.sendto(b'hello', server)
      payload, client_address = sock.recvfrom(1000)
      print("Echoing data back to ", str(client_address), ": ", payload)

      address = payload.decode().split(':')
      address[1] = int(address[1])
      address = ('0.0.0.0', address[1])

      time.sleep(14)
