
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program removes duplicates from a list while maintaining
#              the order of the first occurrence. The original list is
#              unchanged.


def without_duplicates(items):
    """
    Return a list with duplicates removed, keeping the order of first appearance.

    Parameters:
        items (list): List with potential duplicates.

    Returns:
        list: New list with no duplicates.
    """
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list
my_list = [8, 'hello', 8, True, -1000000.4, 'hello', 8]
result = without_duplicates(my_list)
print("List without duplicates:", result)
