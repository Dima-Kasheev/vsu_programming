class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def input_fraction(self):
        self.fraction = input('Type a fraction: ')
        self.numerator, self.denominator = self.fraction.split('/')
        self.numerator, self.denominator = int(self.numerator), int(self.denominator)

    def __nod(self):
        a = abs(self.numerator)
        b = abs(self.denominator)
        while a and b:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b

    def reduce(self):
        nod = self.__nod()
        self.numerator //= nod
        self.denominator //= nod
        if self.numerator < 0 and self.denominator < 0:
            self.numerator, self.denominator = abs(self.numerator), abs(self.denominator)
        elif self.denominator < 0:
            self.numerator, self.denominator = 0 - self.numerator, abs(self.denominator)

    def set_numerator(self, numerator):
        if not isinstance(numerator, int):
            raise ValueError('Numerator must be an integer')
        self.numerator = numerator

    def set_denominator(self, denominator):
        if not isinstance(denominator, int):
            raise ValueError('Denominator must be an integer')
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
