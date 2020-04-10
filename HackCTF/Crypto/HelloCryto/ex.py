import base64
from pwn import *

def KeyRecover():
        key.append(int(ct[0:2], 16) + 256 - 0xEF - (ord('H') ^ ord('H')))       # 1
        key.append(int(ct[2:4], 16) + 256 - 0xEF - (ord('a') ^ ord('e')))       # 2
        key.append(int(ct[4:6], 16) + 256 - 0xEF - (ord('c') ^ ord('l')))       # 3
        key.append(int(ct[6:8], 16) + 256 - 0xEF - (ord('k') ^ ord('l')))       # 4
        key.append(int(ct[8:10], 16) + 256 - 0xEF - (ord('C') ^ ord('o')))      # 5
        key.append(int(ct[10:12], 16) + 256 - 0xEF - (ord('T') ^ ord('C')))     # 6
        key.append(int(ct[12:14], 16) + 256 - 0xEF - (ord('F') ^ ord('r')))     # 7
        key.append(int(ct[14:16], 16) + 256 - 0xEF - (ord('{') ^ ord('y')))     # 8

        key.append(int(ct[72:74], 16) + 256 - 0xEF - key[2])                    # 9
        key.append(int(ct[74:76], 16) + 256 - 0xEF - key[3])                    # 10
        key.append(int(ct[76:78], 16) + 256 - 0xEF - key[4])                    # 11
        key.append(int(ct[78:80], 16) + 256 - 0xEF - key[5])                    # 12
        key.append(int(ct[80:82], 16) + 256 - 0xEF - key[6])                    # 13
        key.append(int(ct[82:84], 16) + 256 - 0xEF - key[7])                    # 14
        log.success("Key has been recovered")


def Decrypt():
        for i in range(len(ct) / 2):
                start = 2 * i
                end = 2 * i + 2
                letter = (int(ct[start : end], 16) + 256 - 0xEF - key[i % len(key)]) ^ ord(strxor_key[i% len(strxor_key)])
                if letter < 0:
                        letter += 128
                flag.append(letter)


        flagg = ""
        for i in range(len(flag)):
                flag[i] = chr(flag[i])
                flagg += flag[i]

        log.success(flagg)


ct = "MjAxZTMwMjE1MDMxNTYxYzUyMjAzNjY0MzE3ZDUzNzg1MTQ3MmU1YTRkMjQxYjMwMzU3OTZlMGY3ZjRkNDQyYjMwNGY1MzQ1NTE0NTU1NTc1MzRjNTA0NTUyNTc1NTRj"
ct = base64.b64decode(ct).decode("UTF-8")

key = []
flag = []
strxor_key = "HelloCrypto"

KeyRecover()
Decrypt()
