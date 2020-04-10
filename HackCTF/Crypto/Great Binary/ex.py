def binToChar(value):
        assert type(value) == str
        num = 0
        for i in range(len(value)):
                num += int(value[len(value) - i - 1]) * pow(2, i)
        return str(chr(num))

binary = "\
01001000 01100001 01100011 01101011 \
01000011 01010100 01000110 01111011 \
01100011 01110010 01111001 01110000 \
01110100 01101111 01011111 01110110 \
00110010 01110010 01111001 01011111 \
01100101 01100001 01110011 01111001 \
01011111 01110000 01110010 00110000 \
01100010 00110001 01100101 01101101 01111101".split(" ")

flag = "".join(binToChar(binary[i]) for i in range(len(binary))) 

print(flag)
