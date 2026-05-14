"""
Problem 4 - Largest Palindrome Product
"""
"""
solution:

    key characteristic of a 6-digit palindrome is it is divisable
    by 11. therefor it cuts search time by 90% (10 digits to search)
    another key method of the algorithm is we start from the top,
    i.e. search for the largest palindrome from the begining.
    (example from the description: 9,009 = 91 x 99, so we
    start attempting from 99 x 99 downwards.)

    another method is generating 6-digit palindromes starting from the top and then check if they are a product of two 3-digit numbers.

"""

# :func: lpp(): checks for largest palindrome from 3-digit products
# :param: n: int 
# :rtype: int: largest product of two 3-digit products

# :helper func: is_palindrome(): check if n is palindrome
# :param: n: int
# :rtype: boolean: True if palindrome, False otherwise

# :author: th4l3s

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def lpp():
    
    largest = 0
    
    for i in range(999,100,-1):
        if i%11==0:
            start = 999
            step = 1
        else:
            start = 990
            step = 11

        for j in range(start, 99, -step):
            prod = i*j
            if prod <= largest:
                break
            if is_palindrome(prod):
                largest = prod
    
    return largest
            

def main():
    print("\nProblem 4 - Largest Palindrome Product\n")
    largest = lpp()
    print(f"Largest palindrome: {largest}")

# Usage:
if __name__ == "__main__":
    main()
