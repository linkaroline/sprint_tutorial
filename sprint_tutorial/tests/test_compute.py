""" Tests for the compute module
"""

from sprint_tutorial.compute import my_sum, my_power
import pytest

def test_my_sum():
    assert my_sum(0, 0) == 0
    assert my_sum(3, 0) == 3


def test_my_pow():
    assert my_power(2, 4) == 16
    assert my_power(5, 2) == 25
