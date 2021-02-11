from hacksport.problem import *
from Crypto.Util.number import getPrime
import os

class Problem(Remote):
  program_name = "PrimeStore.py"
  files = [File("PrimeStore.py"), ProtectedFile("flag.txt"), ProtectedFile("primes1.txt"), ProtectedFile("primes2.txt")]
  def generate_flag(self, random):
      hexdigits = hex(random.randrange(16 ** 8))[2:]
      return "gunnHacks{fact0red_m0du1us_" + hexdigits + '}'
  def setup(self):
    print(os.path.dirname(os.path.realpath(__file__)))
    with open("primes1.txt", "w") as f:
      for i in range(10):
        f.write(str(getPrime(1024)) + "\n")

    with open("primes2.txt", "w") as f:
      for i in range(10):
        f.write(str(getPrime(1024)) + "\n")






