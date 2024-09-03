import pytest
from money import Money
from bank import Bank
from sum import Sum
from franc import Franc


def test_dollar_muliplication():
    five = Money.dollar(5)
    assert Money.dollar(10).equals(five.times(2))
    assert Money.dollar(15).equals(five.times(3))

def testEquality():
    assert True == Money.dollar(5).equals(Money.dollar(5))
    assert False == Money.dollar(5).equals(Money.dollar(6))
    assert False == Money.franc(5).equals(Money.dollar(5))

def testSimpleAddition():
    five = Money.dollar(5)
    sum = five.plus(five)
    bank = Bank()
    redueced = bank.reduce(sum, "USD")
    assert True == Money.dollar(10).equals(redueced)

def testPlusReturnsSum():
    five = Money.dollar(5)
    sum = five.plus(five)
    assert five == sum.augend
    assert five == sum.addend

def testReduceSum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert True == Money.dollar(7).equals(result)

def testReduceMoney():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1).equals(result)

def testReduceMoneyDifferentCurrency():
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1).equals(result)
 