from sympy import randprime

flag = b"GHCTF{ch0s3n_ciph3rt3xt_4tt4ck}"

p = randprime(2 ** 1023, 2 ** 1024)
q = randprime(2 ** 1023, 2 ** 1024)
n = p * q

e = 2 ** 16 + 1

c = [pow(c, e, n) for c in flag]

print("n =", n)
print("e =", e)
print("c =", c)

print("\n\n" + '-' * 50 + "testing:" + '-' * 50)
from utils.rsa.rsa_util import plaintext_pq
assert ''.join([chr(plaintext_pq(x, e, p, q)) for x in c]) == flag.decode()
print(''.join([chr(plaintext_pq(x, e, p, q)) for x in c]))
