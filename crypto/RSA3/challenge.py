from hacksport.problem import Challenge, File

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

class Problem(Challenge):
    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{sm0l_e_" + hexdigits + "}"

    def setup(self):
        generate_challenge(self.flag)
        self.files = [File("rsa3.txt"), File("rsa3.py")]
