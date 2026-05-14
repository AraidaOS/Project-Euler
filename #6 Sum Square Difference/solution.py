"""
Problem 6 - Sum Square Difference

"""

"""
solution:
  - calculate the sum of squares from 1 to LIMIT.
  - calculate the squares of sum from 1 to LIMIT.
  - get the difference by subtracting the max from the min.
"""

# :func: sum_squares(): get sum of squares
# :param: limit:first 100 natural numebrs
# :rtype: int: sum of the squares from 1 -> limit
# :author: th4l3s


def squares_sum(limit):
    sumsq = 0
    for i in range(limit):
        sumsq += pow(i, 2)
    return sumsq


def sum_squares(limit):
    sqsum = 0
    for i in range(limit):
        sqsum += i
    return pow(sqsum, 2)


def main():
    limit = 101
    sumsq = sum_squares(limit)
    sqsum = squares_sum(limit)
    diff = abs(sumsq - sqsum)
    print(f"sum of squares: {sumsq}")
    print(f"squares of sum: {sqsum}")
    print(f"difference is: {diff}")

# Usage:
if __name__ == "__main__":
    main()
