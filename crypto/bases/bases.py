from base64 import b64encode
from binascii import hexlify


def generate_challenge(flag):
    enc = b64encode(flag.encode())
    enc = hexlify(enc)
    enc = list([str(c) for c in enc])
    enc = ' '.join(enc) + '\n'

    with open("bases.txt", "w") as f:
        f.write(enc)
