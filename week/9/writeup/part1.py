#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string


wordlist = open("probable-v2-top1575.txt", 'r')
hashes = open("hashes",'r')
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
	for password in wordlist.readlines():
		test = salt + password.strip()
		pas = hashlib.sha512(test.encode('utf-8'))
		for hashed_pass in hashes.readlines():
			if pas.hexdigest() == hashed_pass.strip():
				print("Hash: %s|Salted password: %s \n" % (hashed_pass,test))
		hashes.seek(0)
	wordlist.seek(0)
		
				
			


