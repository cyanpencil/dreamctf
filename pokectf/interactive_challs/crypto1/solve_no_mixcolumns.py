from pwn import *

import itertools
blocks = lambda x: list(map(bytes, zip(*[iter(x)] * 16)))

if args.LOCAL:
    io = process(["python", "./almost_encryption_standard.py"])
else:
    io = remote(args.HOST, args.PORT)

io.recvline()
flag = bytes.fromhex(io.recvline().decode())

def encrypt(x):
    io.sendline(x.hex())
    c = bytes.fromhex(io.recvline().decode())
    iv = c[:16]
    c = c[16:32]
    return iv, c

p1 = b"0123456789abcdef"
iv1, c1 = encrypt(p1)

p2 = b"ABCDEFGHIJKLMNOP"
iv2, c2 = encrypt(p2)

ps = []
keystream = b""
for offset in range(0, 16, 4):
    print("at offset", offset)
    ok = False
    for perm1 in itertools.permutations(range(4)):
        for perm2 in itertools.permutations(range(4)):
            a1 = [iv1[offset + i] for i in perm1]
            b1 = [c1[offset + i] for i in perm2]
            a2 = [iv2[offset + i] for i in perm1]
            b2 = [c2[offset + i] for i in perm2]
            ks = xor(a1, b1, p1[offset:offset + 4])
            if xor(a1, b1, p1[offset:offset + 4]) == xor(a2, b2, p2[offset:offset + 4]):
                keystream += ks
                ps.append((perm1, perm2))
                ok = True
                break
        if ok:
            break

def dd(iv, ct):
    for offset, (perm1, perm2) in zip(range(0, 16, 4), ps):
        iv = iv[:offset] + bytes([iv[offset + i] for i in perm1]) + iv[offset+4:]
        ct = ct[:offset] + bytes([ct[offset + i] for i in perm2]) + ct[offset+4:]
    return xor(ct, iv, keystream)

def decrypt(ct):
    iv, *bl = blocks(ct)
    r = b""
    for b in bl:
        r += dd(iv, b)
        iv = b
    return r
print(decrypt(flag))
