from hacksport.problem import Challenge, File

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

    with open("rsa2.txt", 'w') as f:
        f.write(f"n={n}\ne={e}\nc={c}\n")

class Problem(Challenge):
    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{brut3!_" + hexdigits + '}'

    def setup(self):
        generate_challenge(self.flag)
        self.files = [File("rsa2.txt"), File("rsa2.py")]
