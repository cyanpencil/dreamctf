from Crypto.Util.number import getPrime
from math import gcd
with open("flag.txt", "rb") as f:
    flag = int.from_bytes(f.read(), "big")

p = getPrime(1024)
q = getPrime(1024)
N = p * q
lam = (p - 1) * (q - 1) // gcd(p - 1, q - 1)
e = lam + 1
c = pow(flag, e, N)
assert c == flag

with open("crypto3_out.txt", "w") as f:
    f.write(f"N = {N}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
