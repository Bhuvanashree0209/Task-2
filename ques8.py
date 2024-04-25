def find_minimum_element(sorted_list):
    # Check if the list is empty
    if not sorted_list:
        return None
    else:
        # Minimum element is the first element of the sorted list
        return sorted_list[0]

# Example sorted list
sorted_list = [1, 3, 5, 7, 9]

# Find the minimum element
min_element = find_minimum_element(sorted_list)
print("Minimum element in the sorted list:", min_element)
