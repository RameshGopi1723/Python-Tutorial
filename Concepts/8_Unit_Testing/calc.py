def add(a: float, b: float) -> float:
    """
    Description:
        Function for adding to numbers

    Args:
        a (float): First value to add
        b (float): Second value to add

    Returns:
        float: The sum of a and b

    Example:
        >>> add(10,5)
        15.0
    """
    return a + b


def sub(a: float, b: float) -> float:
    """
    Description:
        Function for Subtracting two numbers

    Args:
        a (float): First value to sub
        b (float): Second value to sub

    Returns:
        float: The sub of a and b

    Example:
        >>> sub(10,5)
        5.0
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Description:
        Function for multiple two numbers

    Args:
        a (float): First value to multiply
        b (float): Second value to multiply

    Returns:
        float: The multiple of a and b

    Example:
        >>> multiply(10,5)
        50.0
    """
    return a * b


def division(a: float, b: float) -> float:
    """
    Description:
        Function for dividing two numbers

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: The Division of a and b

    Example:
        >>> division(10,5)
        2.0
    """
    if b == 0:
        raise ValueError("Denominator should not be Zero...!")

    return a / b
