"""
Problem 16 - Power Digit Sum

2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26.
What is the sum of the digits of the number 2^1000?
"""

"""
solution:
    - compute 2^1000 usint pow().
    - convert n to str.
    - iterate str whilst converting each character to int and summing it in res.
"""

# :author: th4l3s


def solve(exp: int):
    n = pow(2, exp)
    s = str(n)
    res = 0
    for c in s:
        res += int(c)
    return res

def main():
    exp = int(input("Enter exponent to test: "))
    solution = solve(exp)
    print(f"Solution: {solution}")


# Usage:
if __name__ == "__main__":
    main()
