def find_divisible_by_five(lst):
    divisible_numbers = []
    for num in lst:
        if num % 5 == 0:
            divisible_numbers.append(num)
    return divisible_numbers

# Example usage
my_list = [5, 12, 14, 18, 20, 25, 10]
divisible_numbers = find_divisible_by_five(my_list)
print("Numbers divisible by 5:", divisible_numbers)
