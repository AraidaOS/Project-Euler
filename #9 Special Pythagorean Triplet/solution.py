"""
Problem 9 - Special Pythagorean Triplet
"""

"""
solution:
    we want to find a Pythagorean triplet (a, b, c) such that:

        a^2 + b^2 = c^2
        a + b + c = S

    instead of brute forcing all possible (a, b, c),
    we use Euclid's formula for generating Pythagorean triplets:

        a = m^2 - n^2
        b = 2mn
        c = m^2 + n^2

    where:
        m > n > 0

    now compute the sum:

        a + b + c
        = (m^2 - n^2) + 2mn + (m^2 + n^2)

    the (-n^2) and (+n^2) cancel:

        = 2m^2 + 2mn
        = 2m(m + n)

    so if the desired sum is S, then:

        2m(m+n) = S

    divide by 2:

        m(m+n) = S/2

    so the entire problem becomes:

    Find integers m and n such that
        m(m+n) = S/2
        m > n > 0

    which means:
        m must be a divisor of (S/2)

    so instead of searching for (a, b, c),
    we only search for divisors of S/2.

    this reduces complexity from O(S^2) to O(sqrt(S))

"""

# :func: get_py_triplet(S): return product of triplet a,b,c
# :param: S: int = 1000
# :rtype: int: product of a*b*c

# :author: th4l3s

import math

def get_py_triplet(S):
    
    if S % 2 != 0:
        return None

    target = S // 2
    for m in range(1, int(math.sqrt(target)) + 1):
        if target % m == 0:
            k = target // m
            n = k - m

            if n > 0 and m > n:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n

                return a * b * c
    return None


def main():
    print("\nProblem 9 - Special Pythagorean Triplet\n")
    res = get_py_triplet(1000)
    print(f"Product of a x b x c: {res}")

# Usage:
if __name__ == "__main__":
    main()
