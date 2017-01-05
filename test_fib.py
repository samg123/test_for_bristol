from fib import *

def test_fib():
    n = 0
    expected = 1
    calc = fib(n)
    assert expected == calc

def test_fib():
    n = 1
    expected = 1
    calc = fib(n)
    assert expected == calc

def test_fib():
    n = 6
    expected = 13
    calc = fib(n)
    assert expected == calc


def test_fib():
    n = 7
    expected = 21
    calc = fib(n)
    assert expected == calc
