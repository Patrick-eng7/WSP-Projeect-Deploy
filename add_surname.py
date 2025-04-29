
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program adds "Kardashian" to first names that start
#              with the letter "K" using list comprehension.




def add_surname(names):
    return [name + " Kardashian" for name in names if name.startswith('K')]


