"""
Problem 5 - Smallest Multiple
"""

""" solution:
        Using LCM - least common multiple
        for ease of use, we will use also the gcd function
        so, GCD-LCM method will get the optimal result without
        using any external tools for this challenge.

"""

# :func: smallest_multiple(): get the lcm() in range(1, 20)
# :param: r: range(1, 20)
# :rtype: int

# :helper func: gcd(a, b): Euclidean Algorithm - greatest common divisor
# :param: a,b: two integers to find their GCD
# :rtype: int

# :helper func: lcm(): least common multiple
# :param: a, b: two integers to find their LCM

# :author: th4l3s

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# LCM formula
def lcm(a, b):
    return a * b // gcd(a, b)


def smallest_multiple(r):
    res = 1
    for i in range(1, r+1):
        res = lcm(res, i)
    return res


def main():
    print("\nProblem 5 - Smallest Multiple\n")
    r = 20
    res = smallest_multiple(r)
    print(f"smallest multiple: {res}")

# Usage:
if __name__ == "__main__":
    main()
