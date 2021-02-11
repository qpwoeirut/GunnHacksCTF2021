from math import gcd
from Crypto.Util.number import getPrime

flag_text = open("flag.txt", 'r').read()
flag = int.from_bytes(flag_text.encode(), "big")


def send_new_cipher():
    p = getPrime(1024)
    q = getPrime(1024)
    e = 0x11
    while gcd(e, (p - 1) * (q - 1)) != 1:
        p = getPrime(1024)
        q = getPrime(1024)

    n = p * q

    assert flag < n, f"{flag} {n}"
    c = pow(flag, e, n)

    print("n =", n)
    print("e =", e)
    print("c =", c)


def main():
    print("I'm giving out 100 free encrypted messages! Try to decrypt and guess my message!")
    for i in range(100):
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

    print("Look, I've repeated myself a hundred times already. I'm getting tired of this.")


if __name__ == '__main__':
    main()
