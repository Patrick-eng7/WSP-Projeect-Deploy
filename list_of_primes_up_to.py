# Name: Patrick K.
# GitHub Username: Patrick-eng7
# Date: 5/14/2025
# Description: This program defines a function named list_of_primes_up_to that
#              returns a list of all prime numbers up to a given limit using
#              the Sieve of Eratosthenes algorithm. The default limit is 100.
#              The function constructs a list of boolean values representing
#              primality and iteratively eliminates non-prime indices.
# list_of_primes_up_to.py

def list_of_primes_up_to(limit=100):
    # Step 1: Initialize a list with True values, except for indices 0 and 1
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    # Step 2 onward: Use the Sieve of Eratosthenes
    divisor = 2
    while divisor <= limit ** 0.5:
        if is_prime[divisor]:
            # Mark all multiples of the divisor as not prime
            for multiple in range(divisor * 2, limit + 1, divisor):
                is_prime[multiple] = False
        # Move to the next potential divisor
        divisor += 1

    # Step 6: Use list comprehension to get indices of all True values (i.e., primes)
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

