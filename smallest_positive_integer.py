# This algorithm sorts the input array and then iterates through the sorted array to find the smallest missing positive integer. 
# It starts with 1 (the smallest positive integer) and increments it each time the current integer is found in the array, 
# thus ensuring that the first missing positive integer is returned.


def solution(A):
    # Initialize the smallest missing integer to 1
    smallest_missing = 1
    # Sort the array and iterate through the elements
    for x in sorted(A):
        # If we find the smallest missing integer, increment it
        if x == smallest_missing:
            smallest_missing += 1
    return smallest_missing

# Example usage:
# A = [1, 3, 6, 4, 1, 2]
# print(solution(A))  # Should return 5
# A = [1, 2, 3]
# print(solution(A))  # Should return 4
# A = [-1, -3]
# print(solution(A))  # Should return 1
