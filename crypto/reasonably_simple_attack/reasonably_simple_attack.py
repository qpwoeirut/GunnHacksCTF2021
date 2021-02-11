from math import gcd
from Crypto.Util.number import getPrime


def generate_challenge(flag):
    m = int.from_bytes(flag.encode(), "big")

    p = getPrime(256)
    q = getPrime(24)

    e = 0x10001
    while gcd(e, (p - 1) * (q - 1)) != 1:
        p = getPrime(256)
        q = getPrime(24)

    n = p * q
    assert m < n, f"{m} {n}"
    c = pow(m, e, n)

    with open("reasonably_simple_attack.txt", 'w') as f:
        f.write(f"n={n}\ne={e}\nc={c}\n")
