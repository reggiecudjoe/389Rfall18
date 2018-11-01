#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def print_type_len(t,l):
	print("SECTION TYPE: %s" %t)
	print("SECTION LENGTH: %d" %l)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

SECTION_PNG = 0x1
SECTION_DWORDS = 0x2
SECTION_UTF8 = 0x3
SECTION_DOUBLES = 0x4
SECTION_WORDS = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_ASCII = 0x9
if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, time = struct.unpack('<LLL', data[0:12]) 
author = data[12:20]
num_sections = int(struct.unpack('<L',data[20:24])[0])
if(num_sections <=0):
	bork("Bad section number! Less then zero")
time = datetime.datetime.fromtimestamp(int(time))
off = 24

# Verify author
try:
	decoded_author = author.decode('ascii')
except UnicodeDecodeError:
 	bork("Bad author! Not ascii encoded")
for i in range(len(author)):
	# Loop until the end of the string 
	if author[i] == 0:
		for char in range(i, len(author)):
			if author[char] != 0:
				bork("Bad author! not null padded to 8 bytes")

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %s" %time )
print("AUTHOR: %s" % author.decode('ascii'))
print("SECTIONS: %s" % int(num_sections))
# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
num = 1
while off < len(data):
	print("\nSECTION %d" % num)
	section_type, section_length = struct.unpack('<LL', data[off:off+8])
	off += 8
	if section_type == SECTION_PNG:
		print_type_len("PNG",section_length)
		file_name = "section" + str(num) + ".png"
		print("Png printed %s", file_name)
		with open(file_name,'wb') as file:
			file.write(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')	
			file.write(data[off:off+section_length])
	elif section_type == SECTION_DWORDS:
		print_type_len("DWORDS",section_length)
		if section_length % 8 :
			bork("dwords section length not divisble by 8")
		sval = struct.unpack("<" + "Q" *int(section_length/8),data[off:off+section_length])
		print("Svalue:",sval)
	elif section_type == SECTION_UTF8:
		print_type_len("UTF8",section_length)
		sval = data[off:off+section_length]
		try:
			print("SValue:",sval.decode('utf-8'))
		except UnicodeDecodeError:
			bork("UTF8 section does not contain UTF encoded text")
	elif section_type == SECTION_DOUBLES:
		print_type_len("DOUBLES",section_length)
		if section_length % 8:
			bork("Doubles Section not divisible by 8")
		sval = struct.unpack("<" + "d"*(section_length/8),data[off:off+section_length])
		print("SValue:{}",sval)
	elif section_type == SECTION_WORDS:
		print_type_len("WORDS",section_length)
		if section_length % 4:
			bork("Words not divisble by 4")
		sval = struct.unpack("<" + "L"*int((section_length/4)),data[off:off+section_length])
		print("SValue:",sval)
	elif section_type == SECTION_COORD:
		print_type_len(section_type,section_length)
		if section_length != 16:
			bork('Coord size not equal to 16')
		lat, lon = struct.unpack('<dd', data[off:off+section_length])
		print('(%f,%f)'%(lat,lon))
	elif section_type == SECTION_REFERENCE:
		print_type_len("REFERENCE",section_length)
		if section_length !=4:
			bork("Reference size not eqal to 4")
		sval = struct.unpack("<L",data[off:off+section_length])[0]
		if sval < 0 or sval > num_sections:
			bork("Reference section value %d outside of bounds" % sval)
		print("SValue:",sval)
	elif section_type == SECTION_ASCII:
		print_type_len("ASCII",section_length)
		sval = data[off:off+section_length]
		for char in sval:
			if char < 0 or char > 127:
				bork("Section outside of ASCII range")
		print("SValue:",sval.decode('ascii'))
	else:
		bork('Invalid Section type')
	
	off +=section_length
	num +=1