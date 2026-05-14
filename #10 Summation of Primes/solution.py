"""
Problem 10 - Summation of Primes
"""
"""
solution:
    brute force method - beginner friendly
    check all primes up to 2,000,000 and sum them
    return the sum afterwards.

"""

# :func: helper function is_prime(n) to check if n is prime
# :param: n: int
# :rtype: TRue if n is prime, False otherwsie

# :func: get_sum_primes(limit) return the sum of all primes up to limit
# :param: limit: int 2,000,000
# :rtype: int: sum of all primes up to limit

# :author: th4l3s

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def get_sum_primes(limit):
    sop = 0
    for i in range(2, limit):
        if is_prime(i):
            sop += i
    return sop


def main():
    limit = 2000000
    print("\nProblem 10 - Summation of Primes\n")
    res = get_sum_primes(limit)
    print(f"sum of primes up to {limit}: {res}")

# Usage:
if __name__ == "__main__":
    main()
