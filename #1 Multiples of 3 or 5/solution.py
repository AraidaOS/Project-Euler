"""
Problem 1 - Multiples of 3 and 5

if we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. the sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
"""
solution:
  - check from 1 up to LIMIT if number is divisible by 3 or 5 but NOT both.
  """

# :author: th4l3s

def mulof35(limit):
    som = 0
    for i in range(1, limit):
        if (i%3==0 or i%5==0) :
            som += i
    return som

def main():
    limit = 1000
    res = mulof35(limit)
    print(f"sum of all multiples of 3 or 5 below {limit}: {res}")

if __name__ == "__main__":
    main()
