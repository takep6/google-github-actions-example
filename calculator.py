
def add(a: float, b: float) -> float:
    """Adds two floating point numbers and returns the result.

    Args:
        a: The first floating point number.
        b: The second floating point number.
    Returns:
        The sum of the two floating point numbers.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts two floating point numbers and returns the result.

    Args:
        a: The first floating point number.
        b: The second floating point number.
    Returns:
        The difference of the two floating point numbers.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplies two floating point numbers and returns the result.

    Args:
        a: The first floating point number.
        b: The second floating point number.
    Returns:
        The product of the two floating point numbers.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divides two floating point numbers and returns the result. Raises a ValueError if b is zero.

    Args:
        a: The first floating point number.
        b: The second floating point number.
    Returns:
        The quotient of the two floating point numbers.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))
    try:
        print(divide(1, 0))
    except ValueError as e:
        print(e)
