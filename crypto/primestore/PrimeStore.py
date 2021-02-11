#!/usr/bin/env python3
from Crypto.Util.number import bytes_to_long, inverse
from random import choice

def get_primes():
    with open("primes1.txt", "r") as f1, open("primes2.txt", "r") as f2:
        p1 = int(choice(list(f1)))
        p2 = int(choice(list(f2)))
    return (p1, p2)

def gen_pubkey():
    e = 65537
    p, q = get_primes()
    n = p * q
    return (e, n)

def enc_m(m, e, n):
    m = bytes_to_long(m.encode())
    return pow(m, e, n)

def read_flag():
    with open("flag.txt", "r") as f:
        return f.read().strip()

def main():
    e, n = gen_pubkey()
    flag = read_flag()
    ciphertext = enc_m(flag, e, n)
    print(f"n: {n}\ne: {e}\nct: {ciphertext}")

if __name__ == "__main__":
    main()
