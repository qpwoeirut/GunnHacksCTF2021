from sympy import randprime

flag = int.from_bytes(b"GHCTF{sm0l_e}", "big")

P2 = 868
p = randprime(2 ** P2, 2 ** (P2 + 1))
q = randprime(2 ** P2, 2 ** (P2 + 1))
n = p * q

e = 2**4 + 1

assert pow(flag, e) < n, f"{pow(flag, e)} {n}"
c = pow(flag, e, n)

print("n =", n)
print("e =", e)
print("c =", c)

print("\n\n" + '-' * 50 + "testing:" + '-' * 50)
from utils.rsa.rsa_util import plaintext_pq
from utils.basics import hex_to_ascii
assert plaintext_pq(c, e, p, q) == flag
print(hex_to_ascii(plaintext_pq(c, e, p, q)))
