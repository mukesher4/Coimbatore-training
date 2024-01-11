from Crypto.Util.number import *
from sympy import nextprime 
flag = b"cyberolympics{###stop_hoping_to_find_the_flag_here###}"

p = getPrime(1024)
q = getPrime(1024)

m = bytes_to_long(flag)
e = 3
n = p * q

assert pow(m,e) < n

ct = pow(m,e,n)

f = open("ciphertext.txt", "w")
f.write(f"ct : {ct}\n")

g = open("pubkey.txt", "w")
g.write(f"n : {n}\n")
g.write(f"e : {e}\n")





