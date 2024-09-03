from money import Money

class Bank():
    
    def __init__(self):
        pass

    def reduce(self, source, to):
        if isinstance(source, Money) or issubclass(type(source), Money):
            return source
        return source.reduce(self, to)

    def addRate(self, current, to, rate):
        return 2
