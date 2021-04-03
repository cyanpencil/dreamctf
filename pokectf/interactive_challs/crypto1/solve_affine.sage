import os; os.environ["PWNLIB_NOTERM"] = "1"
from pwn import *

blocks = lambda x: list(map(bytes, zip(*[iter(x)] * 16)))
unpad = lambda x: x[:-x[-1]]
if args.LOCAL:
    def start():
        return process(["python", "./almost_encryption_standard.py"])
else:
    def start():
        return remote(args.HOST, args.PORT)

io = start()
io.recvline()
flag = bytes.fromhex(io.recvline().strip().decode())
nblocks = 12
target = []
M = []
for _ in range(20):
    plain = bytes([randrange(256) for _ in range(nblocks * 16)])
    io.sendline(plain.hex())
    ct = bytes.fromhex(io.recvline().strip().decode())
    iv = ct[:16]
    for p, c in zip(blocks(plain), blocks(ct)[1:]):
        p = xor(iv, p)
        M.append(list(map(int, bin(int.from_bytes(c, "big"))[2:].zfill(128))) + [1])
        target.append(list(map(int, bin(int.from_bytes(p, "big"))[2:].zfill(128))))
        iv = c
M = Matrix(GF(2), M)
target = Matrix(GF(2), target)
transform = M\target
res = b""
iv = flag[:16]
for c in blocks(flag)[1:]:
    v = vector(GF(2), list(map(int, bin(int.from_bytes(c, "big"))[2:].zfill(128))) + [1])
    dec = int(''.join(map(str, v * transform)), 2).to_bytes(16, "big")
    res += xor(dec, iv)
    iv = c
print(unpad(res))
