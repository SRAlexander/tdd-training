class Sum():
    
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        from money import Money
        sum_result = self.augend._amount + self.addend._amount
        return Money(sum_result, to)


