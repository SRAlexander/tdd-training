from sum import Sum 

class Money:

    def __init__(self, value, currency):
        self._amount = value
        self._currency = currency

    @staticmethod   
    def dollar(amount):
        from dollar import Dollar 
        return Dollar(amount, "USD")
    
    @staticmethod 
    def franc(amount):
        from franc import Franc
        return Franc(amount, "CHF")
    
    def plus(self, addend):
        return Sum(self, addend)
    
    def times(self, multiplier):
        return Money(self._amount * multiplier, self.currency)
    
    def equals(self, object):
        classes_match = self._currency == object._currency
        return classes_match and self._amount == object._amount

    def currency(self):
        return self._currency

    def reduce(self, bank, to):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)
    