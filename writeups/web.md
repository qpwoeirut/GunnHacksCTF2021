# GunnHacks 7.0 CTF Web Challenge Writeups

## Default Dilemma
The first thing of interest is a contact form, but a quick check of the Inspect Element Network tab shows that nothing is being sent.
While we're here, let's take a look at the HTML of the page. There's something which sticks out:
```html
<p style="color: rgb(252,253,255);">ayo my slime if you see this go to flag.html for a nice surprise uwu :3</p>
```
Going to `/flag.html` gets us the flag.


## not-brute-force
We get a php source file to look at.
```php
<?php
$pass = $_GET['password'];
$pwd_hash = '0e938161879433076611515433268737'; // you'll never crack my password!
if (!$pass) {show_source("index.php");}
else {
    if (md5($pass) == $pwd_hash) {
        show_source('../flag.txt');
    }
    else {
        echo "Sorry, the password was incorrect!";
    }
}
?>
```
It looks like we give it a password, and then it compares the hash of the password to the hash in the code.
There's no easy way to reverse the hash, but fortunately we can take advantage of a rather stupid PHP behavior.
If PHP tries to compare two different strings that can be converted to numbers, it will convert them to numbers and then compare.
That means that "0" and "0e12345" as considered the same, and "0e123324235" and "0e534346345" are the same as well.
So we need to find a string whose md5 hash can be treated as a number that is equal to 0.
I wrote a program in python to find one.
```python
from hashlib import md5

for i in range(10000000000):
    if i & 1048575 == 0:  # use fancy bitwise tricks to print progress
        print(i)
    hex_hash = md5(str(i).encode()).hexdigest()
    parts = hex_hash.split('e')
    if len(parts) == 2 and parts[0].isdigit() and int(parts[0]) == 0 and parts[1].isdigit():
        print("FOUND:", i)
        break
```
This loops through a bunch of numbers, converts them into strings, and gets their md5 hashes.
Then it splits the hash into parts separated by "e".
For the number to be valid, we need 2 parts.
The first part must be equal to 0 and the second part must be a number.
If those conditions are all satisfied, we have a working password.
This script takes a while to run, but in the end we get `240610708`.
Putting this in as the password gets us the flag.

Other working passwords can also be found online, if you search for similar CTF challenge answers.
