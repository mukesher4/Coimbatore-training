from Crypto.Util.number import *

p,q = getPrime(512),getPrime(512)
n = p*q
e = 3

flag = bytes_to_long(b"flag{###m4n_y0u_r3a11y_g0tt4_st0p_l00k1ng_h3r3_th1s_1s_n0t_th3_fl4g###}")

c = pow(flag,e,n)
f = open("output.txt","w")
f.write(f"n = {n}\n")
f.write(f"e = {e}\n")
f.write(f"c = {c}\n")
f.close()
