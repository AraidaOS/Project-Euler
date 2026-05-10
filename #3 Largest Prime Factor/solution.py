"""
Problem 3 - Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""

# :author: th4al3s

def get_primest_factor(n):
    # check for 2's (only work if n is even, but no harm in check)
    factors = []
    while n%2==0:
        factors.append(2)
        n//=2

    # check for odd factors
    # need to check up to sqrt(n)
    i = 3
    while i*i<=n:
        while n%i==0:
            factors.append(i)
            n//=i
        i+=2    # next odd number

    # if n is remainder, it is last factor
    if n>1:
        factors.append(n)
    
    return factors


def main():
    n = 600851475143
    print(f"\nThis program checks for largest prime factor for {n}\n")
    lf = max(get_primest_factor(n))
    print(f"Largest Prime Factor: {lf}")

# Usage:
if __name__ == "__main__":
    main()
