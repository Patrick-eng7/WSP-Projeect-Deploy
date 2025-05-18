# Name: Patrick K.
# GitHub Username: patrick-eng7
# Date: 5/18/2025
# Description: This program defines a function named square_list that takes a list
#              of numbers as input and mutates it by replacing each value with its square.
#              The function does not return anything and modifies the original list in place.

def square_list(nums):
    """
    Mutates the input list by squaring each number in the list.

    Parameters:
    nums (list): A list of numbers to be squared.

    Returns:
    None
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
