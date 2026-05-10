"""
Problem 29 - Distinct Powers

"""

"""
solution:
	- calc all possible a^b within given limit
	- append them to array list
	- convert list to set to remove dupes
	- return length of set

"""

# :author: th4l3s

def solve(limit):
    array_list = []
    for a in range(2, limit+1):
        for b in range(2, limit+1):
            array_list.append(a**b)

    array_set = set(array_list)
    return len(array_set)
    
    
def main():
    print("===== SOlution to problem #29 ======\n\n")
    result = solve(100)
    print(f"Result: {result}")


# Usage:
if __name__ == "__main__":
    main()
