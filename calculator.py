
def add(a, b):
    """This function adds two numbers"""
    return a + b


def subtract(a, b):
    """This function subtracts two numbers"""
    return a - b


def multiply(a, b):
    """This function multiplies two numbers"""
    return a * b


def divide(a, b):
    """This function divides two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))
    print(divide(1, 0))
