#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
	# receive some data	
	data = s.recv(1024).decode("utf-8")
	print(data)
	if "You win!" in data:
		break
	lines = data.split("\n")
	question = lines[len(lines)-2].split(" ")
	sha = question[3]
	curr_hash = question[6].encode('utf-8')
	hash_algorithm = hashlib.new(sha)
	hash_algorithm.update(curr_hash)
	s.send(hash_algorithm.hexdigest().encode('utf-8')+ b"\n")

# close the connection
s.close()
