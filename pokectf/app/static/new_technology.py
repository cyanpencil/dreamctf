from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, getRandomRange
from Crypto.Util.Padding import pad
import hashlib, itertools

from flag import FLAG

def normalize(fac):
    n = 1
    for p, e in fac:
        n *= p**e
    return n

def gen():
    private = []
    for _ in range(5):
        p = getPrime(512)
        e = getRandomRange(1, 4)
        private.append((p, e))
    return private, normalize(private)

def divs(fac, pre=None):
    if pre is None:
        pre = []
    if not fac:
        yield pre
    else:
        p, e = fac[0]
        for i in range(0, e + 1):
            yield from divs(fac[1:], pre + [(p, i)])

def div(a, b):
    b = dict(b)
    res = []
    for p, e in a:
        assert e >= b[p]
        res.append((p, e - b[p]))
    return res

def phi(fac):
    res = 1
    for p, e in fac:
        if not e: continue
        res *= (p**(e - 1)) * (p - 1)
    return res

def deriv(priv):
    res = 0
    for d1 in divs(priv):
        for d2 in divs(d1):
            res += normalize(d2) * phi(d2) * phi(div(d1, d2))
    return res

priv, pub = gen()
key = deriv(priv)
cipher = AES.new(hashlib.sha256(str(key).encode("utf-8")).digest(), AES.MODE_CBC, iv=b"\0" * 16)
ciphertext = cipher.encrypt(pad(FLAG.encode("utf-8"), 16))

print(f"pub: {hex(pub)}")
print(f"ciphertext: {ciphertext.hex()}")

###
# This printed:
#
# pub: 0x8157a3fcd8f9cd3a7afd752282fd86736e8f2198d38a9e19ab7d9b53d3232c60af5eb2d32158a36cdeec4d179026eeac0d0eb8cc91dbfa32641ce484b27ef473b2c8732f30699d0894fcd45a020eef31685c4434f3e666e19a57cfc4809867166591ddd573eabf672c1928371330cb50d20fcfe5fcb2b96a02fe656f0fc5d6b3d8b13b5044c724e55f71eb87a7ba96e26bdeb58b8cea4efa16832c9c1d30f7a7631e71c1cd552b647316987ffc79d85609c13aa081af45932989aec57a51f55c2672be48bf7ffa7504dd758797cb0853e5e5d5ae00a9e8740850b3451696161a249f26f82db2571094d796df4ac8248a6621beb435cfa45b0a80a585aa01e76f8783da37069ed14b9450af217c91e644a8fc88e970eb76ffd43f7a4df0f12bf154cc5c79ba862eb7f20d3e3adf651680ceae1b2b84dc351a753e2dcd255e844efe8b6b152e3927e5198667ab5f50f0c219c2474840531182a629419106bfc465e094657e245027b35f6f84f8f536d4c3099fd3b736337d49ed50b250bcfa1039b731944ecd10692f4127aa660747a98c611eb7f647d2f82e8b8e70d1c8532ec50a30c0130ba06898db27317cea9ac1ed35bbf6609653b6d53576c8b4cc21d25390438bad544d29757e9c48e0760edbf10ade22ae8ffa5bf3d99fcac4c5e3e7f780f5f2ce84dbc94feec10f00523f258ff1aaafcb1cc8e8f66f8d0cb1602f7588c7aec3c10797604d4b776ec92358e5614c53f886e77c58766532c75134a4ea2f4642d186414c81edc1d041f1726b593d24d0662ee6f8cf3f4ce1f7281f3b707a657089d402e5f31f9b02358ab3b5e792b1d32a325cd02a0d3d11d76d36679e4ec53c3da4a0ded2dacf9cd7740aa2fc49bdb093f436d4cfa7f10b7fbac0acbe7f7f5f289411e7f152fd4e92a4b13a2e8abc9c4b34ea4ea87adeb8fd1868c6c859416ad7b1883597174c93bcb6e3ff8e47845f4bbe3caff0125cb643ee4bc6c9d99b0210751e38b6423e8df25a6c2749778de34a7374d833af2b452efa98416b3708001af13e364ef0fc5b41950c0a05760b3e8309d5470140b37535b1d19523b
# ciphertext: 420225e549e1b698d8a6fd84fbf578b2be707968b5d10da0b0b4ac97149d63c517020d38e7758815c14fc80f80527ac2
###
