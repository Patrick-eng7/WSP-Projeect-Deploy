def fall_distance(t):
    """
    Calculate the distance an object falls due to gravity.(I hope :))

    Parameters:
    t (float): The time in seconds that the object has been falling.

    Returns:
    float: The distance in meters that the object has fallen.
    """
    g = 9.8
    d = 0.5 * g * t ** 2
    return d
