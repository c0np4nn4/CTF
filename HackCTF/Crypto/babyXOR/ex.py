from pwn import *

p = remote("ctf.j0n9hyun.xyz", 9001)

def encrypt():
        p.recvuntil("> ")
        p.sendline("1")
        ct = p.recvline()[2:]
        return ct

def key_modify(key_len):
        p.recvuntil("> ")
        p.sendline("2")
        p.recvuntil("key len: ")
        p.sendline(str(key_len))
        p.recvline()

def getChar(ascii_value):
        value = int(ascii_value, 16)
        return value

hint = "HackCTF{"
knownCT = "7d54535b7567201e6f016b3903123b6054444e6d3706401f3a31171353125a5d78474c6f5502401f44164c33"
key = ""

for i in range(8):
        key += str( hex(ord(hint[i]) ^ getChar(knownCT[i * 2 : i * 2 + 2]) ))[2:]

key_modify(12)
Plain20 = (getChar(encrypt()[38:40]) ^ getChar(key[14:16]))

key_modify(11)
key += str( hex(getChar(encrypt()[38:40]) ^ Plain20) )[2:]

key_modify(10)
key += str( hex(getChar(encrypt()[38:40]) ^ Plain20) )[2:]

log.success("Key construct Completed")

plaintext = ""
ciphertext = encrypt()

for i in range(0,88,2):
        plaintext += str(chr(getChar(ciphertext[i:i+2]) ^ getChar(key[i % 20:i % 20 +2])))


log.success("FLAG : " + plaintext)
