from struct import pack, unpack

def Y(n):
	return pow(n * 0xdeadbeef, n * 0xcafebabe, 2 ** 32)

def encrypt(block):
	a, b, c, d = unpack("<4I", block)
	for i in range(32):
		a, b, c, d = b ^ Y(a | Y(c ^ Y(d)) ^ Y(a | c) ^ d), c ^ Y(a ^ Y(d) ^ (a | d)), d ^ Y(a | Y(a) ^ a), a ^ 1234
		a, b, c, d = c ^ Y(d | Y(b ^ Y(a)) ^ Y(d | b) ^ a), b ^ Y(d ^ Y(a) ^ (d | a)), a ^ Y(d | Y(d) ^ d), d ^ 2345
	return pack("<4I", a, b, c, d)

flag = 'HackCTF{This_Is_Fake}'

while len(flag) % 16:
	flag += "#"

ct = "".join(encrypt(flag[i:i+16]) for i in range(0, len(flag), 16))
open("flag_enc", "w").write(ct)
