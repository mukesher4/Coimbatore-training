from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

flag = b"cyberolympics{###not_even_close###}"
key = os.urandom(16)

m = pad(flag,16)

cipher = AES.new(key, AES.MODE_ECB)
ct = cipher.encrypt(m)

f = open("ciphertext.txt", "w")
f.write(f"ct : {ct}\n")

g = open("key.txt", "w")
g.write(f"key : {key}\n")

