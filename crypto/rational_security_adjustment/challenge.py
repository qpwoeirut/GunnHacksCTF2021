from hacksport.problem import Challenge, File
from Crypto.Util.number import getPrime


def generate_challenge(flag):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q

    e = 0x10001

    c = []
    for char in flag:
        c.append(pow(ord(char), e, n))

    with open("rsa4.txt", 'w') as f:
        f.write(f"n={n}\ne={e}\nc={c}\n")

class Problem(Challenge):
    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{ch0s3n_ciph3rt3xt_4tt4ck_" + hexdigits + '}'

    def setup(self):
        generate_challenge(self.flag)
        self.files = [File("rational_security_adjustment.txt"), File("rational_security_adjustment.py")]
