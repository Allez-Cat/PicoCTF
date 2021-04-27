#! /usr.bin/env python

coded = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"

# out = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])



def encode(flag):
	lst = ""
	for i in range(0, len(flag), 2):
		lst += chr((ord(flag[i]) << 8) + ord(flag[i + 1]))

	return ''.join(lst)

# print(encode("this_is_a_flag"))


def decode(coded):
	lst = ""
	for i in range(len(coded)):
		if coded[i]:
			# print(ord(coded[i]) >> 8)
			lst += chr(ord(coded[i]) >> 8)
			lst += chr((ord(coded[i]) - (ord(coded[i]) >> 8) << 8))
		#	print(chr((ord(encoded_string[i]))-((ord(encoded_string[i])>>8)<<8))) 
	return ''.join(lst)

print(decode(coded))