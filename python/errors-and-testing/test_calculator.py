import calculator, pytest

def test_add():
    assert calculator.add(5, 3) == 8
    assert calculator.add(7, 12) == 19

def test_divide_by_zero():
    with pytest.raises(Exception):
        calculator.divide(10,0)