from struct import pack, unpack
def Y(n):
        return pow(n * 0xdeadbeef, n * 0xcafebabe, 2 ** 32)


def decrypt(block):
        a, b, c, d = unpack("<4I", block)
        for i in range(32):
                o_a = a

                d = d ^ 2345
                a = c ^ Y(d | Y(d) ^ d)
                b = b ^ Y(d ^ Y(a) ^ (d | a))
                c = o_a ^ Y(d | Y(b ^ Y(a)) ^ Y(d | b) ^ a)

                o_a = a
                a = d ^ 1234
                d = c ^ Y(a | Y(a) ^ a)
                c = b ^ Y(a ^ Y(d) ^ (a | d))
                b = o_a ^ Y(a | Y(c ^ Y(d)) ^ Y(a | c) ^ d)
        return pack("<4I", a, b, c, d)



ct = open("flag_enc","r")
s = ct.read(1024)
#print(len(s))

pt = "".join(decrypt(s[i:i+16]) for i in range(0, len(s), 16))
#print(pt)

open("flag","w").write(pt)
