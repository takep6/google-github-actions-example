import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    """Test the subtract function."""
    assert subtract(2, 1) == 1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 100) == 0
    assert multiply(1.5, 2) == 3.0

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1
    assert divide(0, 100) == 0
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError):
        divide(1, 0)