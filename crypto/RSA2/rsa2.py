from sympy import randprime, factorint

flag = int.from_bytes(b"GHCTF{brut3!}", "big")

p = randprime(2 ** 127, 2 ** 128)
q = randprime(2 ** 23, 2 ** 24)
n = p * q

e = 2 ** 16 + 1

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
print(factorint(n))
