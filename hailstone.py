def hailstone(n):
    """
    Returns the number of steps it takes for the hailstone sequence to reach 1.

    Parameters:
    n (int): The starting number of the hailstone sequence.

    Returns:
    int: The number of steps to reach 1.
    """
    steps = 0  # Counter for steps

    # Continue until we reach 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2  # If the number is even, divide it by 2
        else:
            n = 3 * n + 1  # If the number is odd, multiply by 3 and add 1
        steps += 1  # Increment the step counter

    return steps
