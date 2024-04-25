def find_non_repeating_elements(nums):
    # Initialize an empty dictionary to store the count of each number
    count_dict = {}

    # Count occurrences of each number in the list
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Initialize an empty list to store non-repeating elements
    non_repeating_elements = []

    # Iterate through the dictionary and add non-repeating elements to the list
    for num, count in count_dict.items():
        if count == 1:
            non_repeating_elements.append(num)

    return non_repeating_elements

# Example list of integers
nums = [1, 2, 3, 4, 1, 2, 5, 6, 3]

# Find non-repeating elements
result = find_non_repeating_elements(nums)
print("Non-repeating elements:", result)
