"""
Problem 7 - 10 001st Prime
"""

"""
solution:
    beginner friendly method - brute forcing,
    i.e. check all primes up to 10,001th prime.

    simple method - sympy.prime
    i.e. prime(n) = nth prime
"""

# :helper func: is_prime(): helper function to check if n is prime
# :param: n: int
# :rtpe: TRue if n is prime, False otherwise

# :func: brute_prime(): brute force prime checks
# :param: n: int
# :rtpe: int: nth prime number

# :func: simple_prime(): simplify prime checks
# :param: n: int
# :rtpe: int: nth prime number

# :author: th4l3s

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

from sympy import prime

def simple_prime(n):
    return prime(n)


"""
def brute_prime(n):
    cnt = 0
    num = 1
    while cnt < n:
        num += 1
        if is_prime(num):
            cnt += 1
    return num
"""

def main():
    #print("\nusing brute force method:\n")
    print("\nusing simple method - sympy.prime\n")
    n = 10001
    #nth_prime_brute = brute_prime(n)
    nth_prime_simple = simple_prime(n)
    print(f"{n}th prime: {nth_prime_simple}")

# Usage:
if __name__ == "__main__":
    main()
