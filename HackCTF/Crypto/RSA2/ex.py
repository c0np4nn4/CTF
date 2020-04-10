'''
n = 675517326695494061190287679557796696358902817969424171685361
  = 804811499343607200702893651293 × 839348502408870119614692320677
  from https://www.alpertron.com.ar/ECM.HTM
'''

from gmpy2 import *

p = 804811499343607200702893651293
q = 839348502408870119614692320677
e = 65537
c = 0xe3712876ea77c308083ef596a32c5ce2d7edf22abbc58657e

n = p * q
phin = (p - 1) * (q - 1)
d = invert(e, phin)
m = hex(pow(c, d, n))

flag = ""
for i in range(2, len(m), 2):
        flag += str( chr( int( m[i:i+2], 16) ) )
print(flag)
