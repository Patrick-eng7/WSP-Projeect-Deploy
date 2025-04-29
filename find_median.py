
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program calculates the median of a list of numbers.
#              It sorts the list and calculates the median, handling both
#              odd and even length lists separately.


def calculate_median(numbers):
    """Calculates the median of a list of numbers.

    Args:
        numbers (list): List of numerical values.

    Returns:
        float: The median value.
    """
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)

    if n % 2 == 0:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    else:
        median = sorted_nums[n // 2]

    return median

