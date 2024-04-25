def min_difference_mangoes_distribution(mangoes, students):
    mangoes.sort()  # Sort the list of mangoes

    min_diff = float('inf')  # Initialize minimum difference to infinity

    # Initialize pointers
    start = 0
    end = students - 1

    # Iterate through the list of mangoes
    while end < len(mangoes):
        # Calculate the difference between the maximum and minimum mangoes in the current distribution
        diff = mangoes[end] - mangoes[start]
        min_diff = min(min_diff, diff)  # Update the minimum difference

        # Move the start pointer to the next bag
        start += 1
        # Move the end pointer to the next bag
        end += 1

    return min_diff

# Test the function
mangoes = [3, 7, 2, 9, 4, 5]
students = 3
result = min_difference_mangoes_distribution(mangoes, students)
print("Minimum difference in mangoes distribution:", result)
