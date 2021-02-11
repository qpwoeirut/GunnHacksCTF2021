from hacksport.problem import Challenge, File

from random import shuffle

def generate_message(flag):
    return ("""
This cipher is called a substitution cipher, since each letter is substituted for another in a one-to-one mapping.
Given enough text, these ciphers are very insecure.
We can figure out which letters have been substituted by comparing the expected frequencies of letters in a language
(usually English) to the frequencies of the enciphered letters in the ciphertext.
Once we have a couple letters figured out, we can start guessing words of the decrypted text, which gives us even more
of the mapping.
This process becomes easier when you know a piece of the plaintext in advance, since you get part of the mapping for free.
For example, this CTF has a standard flag format of gunnHacks{flag}, so you can be pretty sure that gunnHacks will show up.

There are online decoders that can break a straightforward substitution cipher, like guballa.de/substitution-solver and quipqiup.com.
However, those won't (or at least shouldn't) work for the next substitution cipher challenge.
It might be helpful to use Python though, to speed up some parts of the cipher-breaking. """ +

f"Here's your flag: {flag}").strip().replace('\n', ' ').replace('  ', ' ')

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

class Problem(Challenge):
    def generate_flag(self, random):
        hexdigits = random.choices("abcdef", k=8)  # avoid digits since that will cause ambiguity
        return "gunnHacks{cryptanalysis_beats_substitution_" + "".join(hexdigits) + '}'

    def setup(self):
        generate_challenge(self.flag)
        self.files = [File("substitution.txt")]
