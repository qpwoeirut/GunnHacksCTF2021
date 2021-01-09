from sympy import randprime

favorite_primes = [randprime(2 ** 1023, 2 ** 1024) for _ in range(int(1e2))]
print(favorite_primes)
