import pytest

# content of test_main.py

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# 这个测试返回一个失败报告，因为func(3)不返回5，实际返回4