def fib(n):
    """
    Returns the Fibonacci number at the specified position in the sequence.

    Parameters:
    n (int): The position of the desired number in the Fibonacci sequence.

    Returns:
    int: The Fibonacci number at the nth position.
    """
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1 or n == 2:
        return 1

    # Starting values for the Fibonacci sequence
    a, b = 1, 1

    # Loop through the sequence to find the nth Fibonacci number
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
