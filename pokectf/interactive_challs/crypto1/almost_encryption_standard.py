import hashlib, secrets, sys

into = lambda b: list(map(list, zip(*[iter(b)] * 4)))
outof = lambda m: bytes(sum(m, []))
addkey = lambda k, s: [[x ^ y for x, y in zip(a, b)] for a, b in zip(k, s)]
shiftrows = lambda s: [x[i:] + x[:i] for i, x in enumerate(s)]
blocks = lambda x: list(map(bytes, zip(*[iter(x)] * 16)))
xor = lambda a, b: bytes([x ^ y for x, y in zip(a, b)])

def keys(k):
    for i in range(10):
        yield hashlib.sha256(k + k[i:i+1]).digest()[:16]

def pad(x):
    n = 16 - (len(x) % 16)
    return x + bytes([n] * n)

def encrypt(k, b):
    s = addkey(into(k), into(b))
    for k in keys(k):
        s = addkey(into(k), shiftrows(s))
    return outof(s)

def cbc(k, m, f):
    iv = secrets.token_bytes(16)
    res = iv
    for b in blocks(pad(m)):
        iv = f(k, xor(b, iv))
        res += iv
    return res

def pr(*args, **kw):
    print(*args, **kw)
    sys.stdout.flush()

if __name__ == "__main__":
    pr("Welcome.")
    with open("flag.txt", "rb") as f:
        flag = f.read()
    key = secrets.token_bytes(16)
    pr(cbc(key, flag, encrypt).hex())
    for _ in range(20):
        q = bytes.fromhex(input())
        assert len(q) < 200
        pr(cbc(key, q, encrypt).hex())
