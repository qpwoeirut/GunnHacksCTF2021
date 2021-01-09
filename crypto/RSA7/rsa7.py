import random

from sympy import mod_inverse
from crypto.RSA7.favorites import favorite_primes

assert len(favorite_primes) <= 1e2  # TODO generate these offline lol

flag_text = "GHCTF{gcd}"  # TODO this should fit the backstory
flag = int.from_bytes(flag_text.encode(), "big")


def send_new_cipher():
    p, q = random.choices(favorite_primes, k=2)
    print(favorite_primes)
    n = p * q

    e = 65537

    assert flag < n, f"{flag} {n}"
    c = pow(flag, e, n)

    try:
        mod_inverse(e, (p - 1) * (q - 1))
    except ValueError:
        send_new_cipher()
        return

    print("n =", n)
    print("e =", e)
    print("c =", c)


def main():
    print("some sort of backstory")
    for i in range(1000):
        print("1. Repeat the message")
        print("2. Guess the message")

        cmd = input('> ').strip()
        if cmd == '1':
            send_new_cipher()
        elif cmd == '2':
            guess = input("What did I say?\n> ")
            if guess == flag_text:
                print("Correct! Now submit that as your flag!")
            else:
                print("That's not what I said!")
            return
        else:
            print("Invalid command")

    print("Look, I've repeated myself a thousand times already. I'm getting tired of this.")


if __name__ == '__main__':
    main()
