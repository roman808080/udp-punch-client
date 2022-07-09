#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: David Manouchehri <manouchehri@protonmail.com>
# This script will always echo back data on the UDP port of your choice.
# Useful if you want nmap to report a UDP port as "open" instead of "open|filtered" on a standard scan.
# Works with both Python 2 & 3.

import socket
import time

MY_ID=b'1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '132.145.58.228'
server_port = 31337

server = (server_address, server_port)

wait = True
payload = None

sent = sock.sendto(b'Make a me a server ... please.', server)
our_local_addr = sock.getsockname()

print("Client local name: ", our_local_addr)

sock.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(our_local_addr)

print('I hope I am a server now.')
while True:
      payload, client_address = sock.recvfrom(1000)
      print("Getting data back from: ", str(client_address), ": ", payload)

      sent = sock.sendto(b'I know... I know ... my pour client))', client_address)
      print('Wrote an answer to the client', sent)
