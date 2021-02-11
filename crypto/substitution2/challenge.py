from hacksport.problem import Challenge, File
from binascii import hexlify
from random import shuffle

def generate_message(flag):
    return f"""
Hopefully this challenge wasn't solvable with an online decoder.
In this cipher, the text is converted to numbers before being enciphered.
We can still apply the same techniques though.
In fact, if you did both challenges without any online decoders and have some knowledge of ASCII, this challenge might
have been a bit easier than the first.
We know the most common character will be a space, so that gets us two of the ten characters of the mapping.
We can also be fairly certain that most of the message will be lowercase letters, which are all in a certain numeric range.
This helps eliminate unlikely options.

Here's your flag: {flag}
    """.strip().replace('\n', ' ').replace('  ', ' ')

def generate_challenge(flag):
    message = generate_message(flag)

    encoded = hexlify(message.encode()).decode()  # encoding string to bytes and then bytes to string
    hex_chars = "0123456789abcdef"
    shuffled = list(hex_chars)
    shuffle(shuffled)
    shuffled = ''.join(shuffled)

    table = str.maketrans(hex_chars, shuffled)
    ciphertext = encoded.translate(table)

    with open("substitution2.txt", 'w') as f:
        f.write(ciphertext + '\n')



class Problem(Challenge):
    def generate_flag(self, random):
        hexdigits = hex(random.randrange(16 ** 8))[2:]
        return "gunnHacks{m4nu41_crypt4n41y$i$!_" + hexdigits + '}'

    def setup(self):
        generate_challenge(self.flag)
        self.files = [File("substitution2.txt"), File("substitution2.py")]
