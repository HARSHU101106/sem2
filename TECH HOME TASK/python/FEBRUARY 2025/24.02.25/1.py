import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

start_range = int(input())
end_range = int(input())

primes = [i for i in range(start_range, end_range + 1) if is_prime(i)]
twin_primes = [(primes[i], primes[i + 1]) for i in range(len(primes) - 1) if primes[i + 1] - primes[i] == 2]

print("Twin Primes:", twin_primes)
