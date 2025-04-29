
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program adds "Kardashian" to first names that start
#              with the letter "K" using list comprehension.


def add_surname(names):
    """Return a new list with ' Smith' added to each name."""
    return [name + " Smith" for name in names]


def find_median(numbers):
    """Return the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


def has_duplicates(items):
    """Return True if the list contains duplicate values, otherwise False."""
    return len(items) != len(set(items))

