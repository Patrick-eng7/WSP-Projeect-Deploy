
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program adds "Kardashian" to first names that start
#              with the letter "K" using list comprehension.


def add_surname(names):
    """
    Add "Kardashian" as the surname to names starting with 'K'.

    Parameters:
        names (list): A list of first names.

    Returns:
        list: A list of names with 'Kardashian' added to names starting with 'K'.
    """
    return [name + " Kardashian" for name in names if name.startswith('K')]
names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
result = add_surname(names)
print("Names with surname added:", result)
