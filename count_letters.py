# Name: Patrick K.
# GitHub Username: Patrick-eng7
# Date: 5/27/2025
# Description: This program defines a function named count_letters that
#              takes a string as a parameter and returns a dictionary that
#              tabulates how many of each letter is in the string. The count
#              is case-insensitive and only letters are included. The keys of
#              the dictionary are uppercase letters, and non-letter characters
#              are ignored. The function uses the string count() method.

def count_letters(s):
    s = s.upper()  # Convert to uppercase to normalize letter casing
    letter_counts = {}  # Initialize empty dictionary

    for char in s:
        if char.isalpha():  # Only count alphabetic characters
            if char not in letter_counts:
                letter_counts[char] = s.count(char)  # Use count() method

    return letter_counts
