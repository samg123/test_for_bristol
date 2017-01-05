from mean import *

def test_one():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 4
    assert calculated_value == expected_value


def test_two():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value

def test_three():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 10
    assert calculated_value == expected_value

def test_four():
    input = [1, 2, 'c', 4, 5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value
