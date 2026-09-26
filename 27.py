#27.Write a python program To Find the second largest element in a list.
def find_second_largest_simple(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return "There is no unique second largest element"
    unique_numbers.sort()
    return unique_numbers[-2]
nums = [12, 35, 1, 10, 34, 1, 35]
print(f"Second largest element: {find_second_largest_simple(nums)}")
