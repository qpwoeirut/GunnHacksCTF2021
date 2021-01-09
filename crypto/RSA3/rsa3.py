from sympy import randprime

flag = int.from_bytes(b"GHCTF{w@tch_y0ur_3xp0n3nt$!}", "big")

p = randprime(2 ** 120, 2 ** 121)
q = randprime(2 ** 120, 2 ** 121)
n = p * q

e = 1

assert flag < n, f"{flag} {n}"
c = pow(flag, e, n)

print("n =", n)
print("e =", e)
print("c =", c)

print("\n\n" + '-' * 50 + "testing:" + '-' * 50)
from utils.rsa.rsa_util import plaintext_pq
from utils.basics import hex_to_ascii
assert plaintext_pq(c, e, p, q) == flag
print(hex_to_ascii(plaintext_pq(c, e, p, q)))
