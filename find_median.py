
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program calculates the median of a list of numbers.
#              It sorts the list and calculates the median, handling both
#              odd and even length lists separately.


def find_median(numbers):
    """
    Calculate the median of a list of numbers.

    Parameters:
        numbers (list): List of numbers to calculate the median.

    Returns:
        float or int: The median value.
    """
    numbers.sort()
    length = len(numbers)

    if length % 2 == 1:  # Odd length
        return numbers[length // 2]
    else:  # Even length
        mid1 = numbers[length // 2 - 1]
        mid2 = numbers[length // 2]
        return (mid1 + mid2) / 2
numbers = [13, 7, -3, 82, 4]
median = find_median(numbers)
print(f"The median is: {median}")
