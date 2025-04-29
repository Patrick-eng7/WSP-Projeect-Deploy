
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program calculates the median of a list of numbers.
#              It sorts the list and calculates the median, handling both
#              odd and even length lists separately.


# find_median.py

def find_median(numbers):
    # Sort the list first
    numbers.sort()

    # Get the length of the list
    n = len(numbers)

    # If the number of elements is odd, return the middle element
    if n % 2 != 0:
        return numbers[n // 2]
    # If the number of elements is even, return the average of the two middle elements
    else:
        middle1 = numbers[(n // 2) - 1]
        middle2 = numbers[n // 2]
        return (middle1 + middle2) / 2


