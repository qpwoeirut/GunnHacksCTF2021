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
