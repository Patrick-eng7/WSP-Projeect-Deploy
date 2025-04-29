
# Name: Patrick
# GitHub Username: Patrick-eng7
# Date: 4/28/2025
# Description: This program removes duplicates from a list while maintaining
#              the order of the first occurrence. The original list is
#              unchanged.


def remove_duplicates(items):
    """Removes duplicate elements from a list while preserving order.

    Args:
        items (list): List that may contain duplicates.

    Returns:
        list: List with duplicates removed.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

