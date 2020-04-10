import base64
from Crypto.Util.strxor import strxor

key = "****"          
message = "****" 

assert len(key) == 14

strxor_key = "HelloCrypto"
strxor_key = (strxor_key * (len(message) / len(strxor_key) + 1))[:len(message)]
message = strxor(message, strxor_key)

message += key

cipher = ''
for i in range(0, len(message)):
  cipher += chr((ord(message[i]) + ord(key[i % len(key)]) + 0xDEADBEEF) % 128)
  
print base64.b64encode(cipher.encode("hex"))
