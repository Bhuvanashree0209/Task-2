def has_sublist_with_sum_zero(nums):
    cumulative_sum = 0
    sum_map = {}  # Dictionary to store cumulative sums

    for num in nums:
        cumulative_sum += num

        # If cumulative sum is zero or already seen, there's a sublist with sum zero
        if cumulative_sum == 0 or cumulative_sum in sum_map:
            return True

        # Store the cumulative sum in the map
        sum_map[cumulative_sum] = True

    return False  # No sublist with sum zero found

# Example list
nums = [4, 2, -3, 1, 6]

# Check if there is a sublist with sum zero
result = has_sublist_with_sum_zero(nums)
if result:
    print("Yes, there is a sublist with sum zero.")
else:
    print("No, there is no sublist with sum zero.")
