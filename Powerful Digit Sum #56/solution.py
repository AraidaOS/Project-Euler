"""
Problem 56 - Powerful Digit Sum
    A googol (10^100) is a massiv number: one followed by one-hundred zeros;
    100^100 is almost unimaginably large: one followed by two-hundred zeros.
    Despite their size, the sum of each digit is only 1.
    Considering natural numebrs of the form, a^b, where a,b < 100, what is the maximum digital sum?
"""

"""
solution:
    - init mx variable for storing max sum = 0
    - iterate each of a (1, 100) to the power b (1, 100).
    - compare current sum of digits of (a^b), store max in mx
    - return mx in nice format

"""

# :author: th4l3s

# helper function to sum digits of given n
def sum_digits(n: int) -> int:
    return sum(int(d) for d in str(abs(n)))

# solve the problem using the logic we wote in description
def solution():
    mx = 0
    for a in range(1, 100):
        for b in range(1, 100):
            s = sum_digits(pow(a, b))
            if s > mx:
                mx = s
    return mx


def main():
    print(f"Max Sum: {solution()}")


# Usage:
if __name__ == "__main__":
    main()
