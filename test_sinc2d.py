from sinc2d import *
import numpy as np

def test_1():
    expec = 1
    calc = sinc2d(0,0)
    assert calc == expec

def test_2():
    x=1
    expec = np.sin(x) / x
    calc = sinc2d(x,0)
    assert calc == expec

def test_3():
    y = 1
    expec = np.sin(y) / y
    calc = sinc2d(0,y)
    assert calc == expec

def test_4():
    x = 0.5
    y = 0.5
    expec = (np.sin(y) / y) * (np.sin(x) / x)
    calc = sinc2d(x,y)
    assert calc == expec
