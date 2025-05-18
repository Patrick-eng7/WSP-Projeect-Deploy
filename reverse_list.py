# Name: Patrick K.
# GitHub Username: patrick-eng7
# Date: 5/18/2025
# Description: This program defines a function named reverse_list that takes a list
#              as input and reverses the order of its elements by mutating the original list.
#              The function does not return anything and must not use slicing.

def reverse_list(lst):
    """
    Mutates the input list by reversing the order of its elements.

    Parameters:
    lst (list): The list to be reversed.

    Returns:
    None
    """
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
