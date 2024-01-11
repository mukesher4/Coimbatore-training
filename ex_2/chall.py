from Crypto.Util.number import *


flag = b"cyberolympics{###you_really_thought_this_was_the_flag###}"

def get_primes():
    p = getPrime(1024)
    q = getPrime(1024)
    return p, q

p,q = get_primes()
n = p * q
e = 65537

m = bytes_to_long(flag)
ct = pow(m, e, n)

f = open("ciphertext.txt", "w")
f.write(f"ct : {ct}\n")

g = open("keys.txt", "w")
g.write(f"p, q : {p}, {q}\n")
g.write(f"e : {e}\n")

