#!/usr/bin/python3
import codecs
import binascii
def encrypt(flag, key):
	enc = ''
	for i in range(len(flag)):
		enc += chr(ord(key[i % len(key)]) ^ ord(flag[i]))
	return enc

def main():
	key = open('key').read()
	key_len = len(key)
	flag = open('flag').read()

	while (1):
		print ("1. encrypt")
		print ("2. re-generate key")
		print ("3. bye")
		
		choice = input("> ")

		if choice == "1":
                    en = encrypt(flag, key[:key_len])
                    result = binascii.hexlify(en.encode())
                    print (result)
		elif choice == "2":
			length = input("key len: ")
		
			try:
				int(length)

				if int(length) < 8:
					print ("invalid")
				else:
					key_len = int(length)
					print ("Success")
			except:
				print ("invalid")
		elif choice == "3":
			break
		else:
			print ("invalid")
main()
