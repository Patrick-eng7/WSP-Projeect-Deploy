# Name: Patrick K.
# GitHub Username: Patrick-eng7
# Date: 5/14/2025
# Description: This program defines a recursive function named multiply that
#              takes two positive integers as parameters and returns their
#              product using repeated addition. The function does not use any
#              loops or the multiplication operator.

def multiply(a, b):
    # Base case: multiplying by 1 returns the number itself
    if b == 1:
        return a
    # Recursive case: a * b = a + (a * (b - 1))
    return a + multiply(a, b - 1)
