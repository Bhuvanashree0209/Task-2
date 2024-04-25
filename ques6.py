def find_duplicates(list1, list2, list3):
    # Concatenate all three lists into one list
    combined_list = list1 + list2 + list3

    # Initialize an empty set to store duplicates
    duplicates = set()
    seen = set()

    # Iterate through the combined list
    for item in combined_list:
        # If the item is seen before, it's a duplicate
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 9, 10, 11]

# Find duplicates
result = find_duplicates(list1, list2, list3)
print("Duplicates in the lists:", result)
