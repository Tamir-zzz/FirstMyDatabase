import pytest

def sum(a,b):
    n = a + b
    return n

def test_1():
    ss = sum(1,2)
    assert 3 == ss

def test_2():
    ss = sum(-1,2)
    assert 1 == ss

def test_3():
    ss = sum(1,-2)
    assert -1 == ss

def test_4():
    ss = sum(-1,-2)
    assert -3 == ss

