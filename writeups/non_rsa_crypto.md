# GunnHacks 7.0 CTF Non-RSA Cryptography Writeups


## Substitution 1
(This is based on the secret message in the challenge.)

This cipher is called a substitution cipher, since each letter is substituted for another in a one-to-one mapping.
Given enough text, these ciphers are very insecure.
We can figure out which letters have been substituted by comparing the expected frequencies of letters in a language
(usually English) to the frequencies of the enciphered letters in the ciphertext.
For example, the most commonly used letter in English is `e`, which means that the most common letter in the ciphertext probably maps to `e`.
Once we have a couple letters figured out, we can start guessing words of the decrypted text, which gives us even more
of the mapping.

This process becomes easier when you know a piece of the plaintext in advance, since you get part of the mapping for free.
For example, this CTF has a standard flag format of gunnHacks{flag}, so you can be pretty sure that gunnHacks will show up.

This challenge could also have been solved using online decoders like https://www.guballa.de/substitution-solver and https://quipqiup.com/.
Just be careful that flags are case-sensitive, so you need the capitalization to match.
(Sorry for not mentioning that at the start of the CTF.)


## Substitution 2
(This is based on the secret message in the challenge.)

Hopefully this challenge wasn't solvable with an online decoder. (If you found an online decoder for it I'd be very interested -- please contact me.)
In this cipher, the text is converted to numbers before being enciphered.
We can still apply the same techniques though, by analyzing the frequency of pairs of hex characters since each pair corresponds to a letter.

We know the most common character will be a space, so that gets us two of the sixteen characters of the mapping.
We can also be fairly certain that most of the message will be lowercase letters, which are all in a certain numeric range.
This helps eliminate unlikely options.
For example, we can be fairly certain the first hex letter of a pair won't map to a 0, since all the 2-digit hex numbers that start with 0 are control codes in ASCII (meaning they're not printable).

If you did both challenges without any online decoders and have some knowledge of ASCII, this challenge might
have been a bit easier than the first since the mapping has only 16 characters.