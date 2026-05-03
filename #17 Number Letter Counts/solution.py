"""
Problem 17 - Number Letter Counts

"""

"""
solution:
    - convert number from 1 to 1000 to coresponding word.
    - count letters exluding white spaces and special chars.
    - return sum of letters.
    [note] num2words automatically assigns english as def lang
"""

# :author: th4l3s

from num2words import num2words
import string

def solve(w):
    words = num2words(w)
    return sum(1 for c in words if c in string.ascii_letters)
    

def main():
    limit = 1000
    sol = sum(solve(w) for w in range(1, limit+1))
    print(f"Sum of letters in words up to 1000: \n{sol}")

# Usage:
if __name__ == "__main__":
    main()
