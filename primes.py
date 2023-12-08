"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
  if number_of_primes <= 0:
    raise ValueError("number_of_primes must be a positive integer")

  primes = []
  current = 2
  while len(primes) < number_of_primes:
    is_prime = True
    for prime in primes:
      if current % prime == 0:
        is_prime = False
        break

    if is_prime:
      primes.append(current)

    current += 1

  return primes

print(primes(10))
