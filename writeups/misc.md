# GunnHacks 7.0 CTF Misc Challenge Writeups

## Rules Check
Points: 1
> Welcome to GunnHacks 7.0 CTF! For instructions on how to participate in the CTF and important information about prizes, check out the #ctf-instructions channel on the Discord server. (The flag for this challenge will be there too.) If you have any questions about the CTF, please send a DM to chop0#2274 and/or qpwoeirut#5057.

After carefully reading the rules, you'll see the flag at the bottom of the channel.


## Bases
Points: 50
> Let's start off with a base-ic challenge!<br>
> Hint: Try searching online for ASCII, hex encoding, and base64 encoding.

We're given a file with a bunch of space-separated numbers.
Here's an [example](bases.txt) of a file.
(Yours was probably slightly different.)

All these numbers are around 48 to 100.
This is also the range of alphabetical letters under ASCII representation.
We can convert these numbers to their corresponding letters in ASCII.
There are several ways to do this.
The easiest would probably be to use the `From Decimal` recipe in [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Decimal('Space',false)).
This can also be done with Python's builtin `chr` function, which converts the ASCII numeric representation into a letter.
```python
# read the file
with open("bases.txt") as file:
    text = file.read()

numbers = text.split()  # split the text into a list of individual numbers
numbers = [int(n) for n in numbers]  # use a list comprehension to convert from strings into numbers
letters = [chr(c) for c in numbers]  # covert to letters using ASCII
decoded = ''.join(letters)  # join together the letters, with an empty separator
```

This gets us a large string of hex characters. Hex characters are 0 to 9 and a to f.
In this example, we end up with `5a335675626b68685932747a65334d7762544e66596a516b61574e664d32356a4d475270626d64664e444d794d5745795a475239`.
This string is another way to store letters in a different base.
Here, we have a hex encoding.
Every two hex letters corresponds to one decoded letter.
This works out well since we have 16 hex letters, so two hex letters can represent 16*16 = 256 values.
There are also 256 different values in ASCII.

Again, the easiest way to convert is probably with [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')).
This time, we'll use the `Frox Hex` recipe.
We can do this with Python as well.
Continuing from the script above:
```python
parts = [decoded[i:i+2] for i in range(0, len(decoded), 2)]  # split into parts with 2 hex characters each
parts = [int(part, 16) for part in parts]  # convert the hex string into an integer -- hex is base 16
parts = [chr(c) for c in parts]  # same as earlier -- convert the letters using ASCII
hex_decoded = ''.join(parts)  # then join together the letters
```
We could use `binascii.unhexlify` in Python as well for a one-liner.

Decoding the hex yields `Z3VubkhhY2tze3MwbTNfYjQkaWNfM25jMGRpbmdfNDMyMWEyZGR9`.
(Again, yours will probably be slightly different).
This is base64 encoding.
We can use the `From Base64` recipe on [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)) to decode.
This can also be done with Python's `base64` library.
```python
import base64
print(base64.b64decode(hex_decoded))
```

After decoding the base64, we should get the flag.


## Intro to Netcat
Points: 50
> Some of the challenges in the CTF will require you to connect to a server via netcat. Connect to `shell.ctf.gunnhacks.com` at port `45752` to get the flag!

(Note that the port might be different for different people.)

This challenge was meant to introduce contestants to netcat.
On Linux and Mac, typing `nc shell.ctf.gunnhacks.com 45752` will open a connection to the server, which sends you the flag.
For Windows, it's a bit more complicated.
You can enable and then use `telnet`, or you can download `nc` since it's not installed by default.
