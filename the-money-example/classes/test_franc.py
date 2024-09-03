import pytest

from money import Money
from franc import Franc


def test_franc_muliplication():
    five = Money.franc(5)
    assert Money.franc(10).equals(five.times(2))
    assert Money.franc(15).equals(five.times(3))

def testEquality():
    assert True == Money.franc(5).equals(Money.franc(5))
    assert False == Money.franc(5).equals(Money.franc(6))
    assert False == Money.franc(5).equals(Money.dollar(5))
