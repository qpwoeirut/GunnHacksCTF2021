from hacksport.problem import Challenge, File
from base64 import b64encode
from binascii import hexlify


def generate_challenge(flag):
    enc = b64encode(flag.encode())
    enc = hexlify(enc)
    enc = list([str(c) for c in enc])
    enc = ' '.join(enc) + '\n'

    with open("bases.txt", "w") as f:
        f.write(enc)


class Problem(Challenge):
    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{s0m3_b4$ic_3nc0ding_" + hexdigits + '}'

    def setup(self):
        generate_challenge(self.flag)
        self.files = [File("bases.txt")]
