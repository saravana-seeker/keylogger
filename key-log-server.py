#!/usr/bin/env python3

import socket

HOST = '192.168.112.128'
PORT = 65432

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			print('Connected by', addr)
			while True:
				data = conn.recv(1024)
				if not data:
					break
				print(data.decode('utf8'))
