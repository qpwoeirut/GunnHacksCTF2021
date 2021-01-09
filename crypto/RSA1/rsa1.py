from sympy import randprime

flag = int.from_bytes(b"GHCTF{w3lc0m3_t0_RSA}", "big")

p = randprime(2 ** 1023, 2 ** 1024)
q = randprime(2 ** 1023, 2 ** 1024)
n = p * q

e = 2 ** 16 + 1

assert flag < n, f"{flag} {n}"
c = pow(flag, e, n)

print("p =", p)
print("q =", q)
print("n =", n)
print("e =", e)
print("c =", c)

print("\n\n" + '-' * 50 + "testing:" + '-' * 50)
from utils.rsa.rsa_util import plaintext_pq
from utils.basics import hex_to_ascii
assert plaintext_pq(c, e, p, q) == flag
print(hex_to_ascii(plaintext_pq(c, e, p, q)))
