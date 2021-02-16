# GunnHacks 7.0 CTF RSA Writeups

All the provided scripts assume you copy-pasted the provided numbers in each file.
So it will use the variables `n`, `e`, `c`, etc.

## A Really Strange Algorithm
Points: 50
> What do all of these letters mean?

For this challenge, we are given both the public and the private key.
To get the flag, we can follow the decryption steps outlined in https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation.
Here's a python script which uses a python3.8 feature to calculate the modular inverse:
```python
d = pow(e, -1, (p-1) * (q-1))  # we could mod by lcm(p-1, q-1) but since that's a factor of (p-1) * (q-1), either works
m = pow(c, d, n)
print(m.to_bytes(50, 'big'))  # let's just make the size 50 bytes, which should be longer than the flag
```


## A Reasonably Simple Attack
Points: 100
> Let's start off with the most straightforward RSA attack... Try decrypting this message. Here's the code used to generate the encryption: reasonably_simple_attack.py

This time, we don't get the private key.
We are given the script that generated the key and ciphertext though.
Looking at the code, we can see that the largest value that `q` will be is 2<sup>24</sup>.
This is small enough that we can try all values of `q`, and see which one divides `n`.
```python
for i in range(2, n):  # this will stop after q iterations, which is fast enough
    if n % i == 0:
        q = i
        p = n // q
        break
```
Then we can decrypt using the same method as the previous challenge.

There are several other ways that we can find the factors.
There's a Python library called `sympy` that has a `factorint` method, which can find factors more efficiently than a brute force.
The numbers are also small enough that they should appear on [FactorDB](http://factordb.com/), which is a massive database with the factors of numbers.


## A Rather Small Apparatus
Points: 200
> Something seems a bit small here... Source code at rather_small_apparatus.py

`e` is only 13 here, which is so small that the m<sup>e</sup> is smaller than `n`.
This means that the modulus has no effect, so we can take the `e`-th root of the ciphertext.
One simple way to do this is a binary search.
```python
lo, hi = 0, c
while lo < hi:
    mid = (lo + hi) // 2
    if pow(mid, e) < c:
        lo = mid + 1
    elif pow(mid, e) > c:
        hi = mid - 1
    else:
        lo = mid
print(lo.to_bytes(20, 'big'))
```


## A Rational Security Adjustment
Points: 200
> I tried encoding each character of my message with RSA to make sure every single character is secure! Here's the code I used to do it: rational_security_adjustment.py

Encrypting each letter separately makes the encryption vulnerable to a [chosen-ciphertext attack](https://en.wikipedia.org/wiki/Chosen-ciphertext_attack).
Since the amount of possible values that might be encrypted is very small (there's only around 90 different characters that might be encrypted), we can use the provided public key to try encrypting them ourselves.
This allows us to construct a mapping from the plaintext letter to the ciphertext, which we can reverse to get a ciphertext to plaintext mapping.
We can use this mapping to get the flag.
Below is python code to calculate the mapping from the ciphertext to the plaintext.
It uses a dictionary comprehension to quickly create the mapping.
```python
mapping = {pow(i, e, n): chr(i) for i in range(128)}
flag = ""
for char in c:
    flag += mapping[char]
print(flag)
```


## Prime Store
Points: 400
> I’ve devised a revolutionary new method for RSA key generation. Instead of spending precious time computing huge prime factors, why not precompute them, store them in a file, and choose them at random when needed? To prove how secure this is, I’ve made the code available to you and even put an implementation of it on a public server. If you can manage to exploit the server and decrypt its ciphertext, send it to me and I’ll give you a reward.

Let's say we have one key where `n1 = p * q1` and another where `n2 = p * q2`.
Since `n1` and `n2` share a common factor, we can recover `p` by calculating `gcd(n1, n2)`.
Finding the value of `p` will allow us to decrypt the flag.

If you know how to use pwntools, this can be automated.
If not, you can manually copy-paste in the numbers.
The number of unique primes is small enough that you won't need to copy many numbers.
```python
from math import gcd
from pwn import remote

n_list = set()
done = False
while not done:
    r = remote(host, port)  # these differ between challenge instances
    n = int(r.recvline().decode().split(':')[1])
    e = int(r.recvline().decode().split(':')[1])
    c = int(r.recvline().decode().split(':')[1])

    for other_n in n_list:
        if n == other_n:
            continue
        if gcd(n, other_n) > 1:
            p = gcd(n, other_n)
            q = n // p

            d = pow(e, -1, (p-1) * (q-1))
            m = pow(c, e, n)
            print(m.to_bytes(50, 'big'))

            done = True
            break
```

## Repeated Message
Points: 400
> I'm giving out 100 free encrypted messages! Try to decrypt and guess my message! Here's the code running on the server.

This is vulnerable to [Håstad's broadcast attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H%C3%A5stad's_broadcast_attack).
The linked article has a more formal explanation, but the idea of Håstad's broadcast attack is that we can apply Chinese Remainder Theorem over the ciphertexts and moduli.
This ends up with a combined ciphertext `C`, which will be equal to m<sup>e</sup>.
Then we can take the `e`-th root in the same way we did for the `Rather Small Apparatus` challenge.

```python
from functools import reduce
from pwn import remote

r = remote(host, port)  # these differ between challenge instances
r.recvline()

n_list = []
c_list = []

e = 0x11
for i in range(e):
    r.recvline()
    r.recvline()
    r.sendline('1')
    n_list.append(int(r.recvline().decode().split('=')[1]))
    r.recvline()
    c_list.append(int(r.recvline().decode().split('=')[1]))


# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


c = chinese_remainder(n_list, c_list)
lo, hi = 0, c
while lo < hi:
    mid = (lo + hi) // 2
    if pow(mid, e) < c:
        lo = mid + 1
    elif pow(mid, e) > c:
        hi = mid - 1
    else:
        lo = mid
print(lo.to_bytes(20, 'big'))
```