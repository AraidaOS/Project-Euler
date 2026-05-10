"""
Problem 2 - Even Fibonacci Numbers

Each new term in the fibonacci sequence is genertaed by adding the
previous two terms. BY starting with 1 and 2, the first 10 terms
will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the evenvalued terms.

"""

# :func: calculate the sum of first even 4mil fib numbers
# :param: limit: 4,000,000
# :rtype: int: sum of even fib numbers up to limit
# :author: th4l3s

def calcfib(limit):
    f,s = 1,2
    ttl = 0
    while f <= limit:
        if f%2==0:
            ttl += f
        f,s = s, f+s
    return ttl

def main():
    limit = 4000000
    res = calcfib(limit)
    print(f"sum of first {limit} even-vlaued fibonacci numbers: {res}")

# Usage:
if __name__ == "__main__":
    main()
