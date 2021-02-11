from random import shuffle
from secret import generate_message


def generate_challenge(flag):
    message = generate_message(flag)

    chars = ''.join([c for c in set(message) if c.isalpha() and c.islower()])
    shuffled = list(chars)
    shuffle(shuffled)
    shuffled = ''.join(shuffled)
    chars += chars.upper()
    shuffled += shuffled.upper()
    table = str.maketrans(chars, shuffled)
    ciphertext = message.translate(table)

    with open("substitution.txt", 'w') as f:
        f.write(ciphertext + '\n')
