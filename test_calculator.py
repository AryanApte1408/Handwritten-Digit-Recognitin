# test_calculator.py
from calculator import add

def test_add():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_floats():
    assert add(1.5, 2.5) == 4.0
