#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: David Manouchehri <manouchehri@protonmail.com>
# This script will always echo back data on the UDP port of your choice.
# Useful if you want nmap to report a UDP port as "open" instead of "open|filtered" on a standard scan.
# Works with both Python 2 & 3.

import socket
import time

MY_ID=b'1'

server_address = '132.145.58.228'
server_port = 31337
client_port = 22500 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', client_port))

server = (server_address, server_port)

wait = True
payload = None

while wait:
      sent = sock.sendto(MY_ID, server)
      print("Client local name: ", sock.getsockname())

      payload, client_address = sock.recvfrom(1000)
      print("Getting data back from: ", str(client_address), ": ", payload)

      if payload == b's:wait':
            time.sleep(1)
      else:
            wait = False


print("Current payload: ", payload)
resopnse_from_server = payload.decode().split(':')
peer_address = None

if resopnse_from_server[0] == 's' and resopnse_from_server[1] == 'connect':
      print("We have a peer: ", resopnse_from_server[2], resopnse_from_server[3])

      peer_address = (resopnse_from_server[2], int(resopnse_from_server[3]))
      message = b'c:punch'
      attempts = 5

      for _ in range(attempts):
            sent = sock.sendto(message, peer_address)
            print('Message: ', str(message) + " Peer address: ", peer_address, " Sent: ", sent)
            time.sleep(0.5)
else:
      print("Unknown message: ", resopnse_from_server[0], resopnse_from_server[1])
      exit(1)

while True:
      sent = sock.sendto(b'c:hello', peer_address)
      payload, recv_from_addr = sock.recvfrom(1000)
      print("Message recv: ", str(payload), " Expected addr: ", peer_address, " Actual addr: ", recv_from_addr)
      time.sleep(1)
