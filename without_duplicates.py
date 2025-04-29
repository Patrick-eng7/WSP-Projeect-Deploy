
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program removes duplicates from a list while maintaining
#              the order of the first occurrence. The original list is
#              unchanged.


def without_duplicates(input_list):
    # Create an empty list to store results
    result = []
    # Create a set to track seen items
    seen = set()

    # Loop through each element in the input list
    for item in input_list:
        # If the item has not been seen before, add it to the result and mark it as seen
        if item not in seen:
            result.append(item)
            seen.add(item)

    # Return the result list with no duplicates
    return result
