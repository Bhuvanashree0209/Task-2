def find_triplet_with_sum(nums, target):
    nums.sort()  # Sort the list to enable two-pointer technique

    for i in range(len(nums) - 2):  # Iterate till the third last element
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            elif current_sum < target:
                left += 1  # Move left pointer to increase the sum
            else:
                right -= 1  # Move right pointer to decrease the sum

    return None  # If no such triplet is found

# Example list and target value
nums = [10, 20, 30, 9]
target = 59

# Find the triplet with the given sum
result = find_triplet_with_sum(nums, target)
if result:
    print("Triplet with sum", target, ":", result)
else:
    print("No triplet found with sum", target)
