from math import gcd
from Crypto.Util.number import getPrime


def generate_challenge(flag):
    m = int.from_bytes(flag.encode(), "big")

    p = getPrime(1024)
    q = getPrime(1024)

    e = 0x11
    while gcd(e, (p - 1) * (q - 1)) != 1:
        p = getPrime(1024)
        q = getPrime(1024)

    n = p * q
    assert m < n, f"{m} {n}"
    c = pow(m, e, n)

    with open("rsa3.txt", 'w') as f:
        f.write(f"n={n}\ne={e}\nc={c}\n")
