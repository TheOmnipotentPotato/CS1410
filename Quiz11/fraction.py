class Fraction():
    def __init__(self, numerator: int, denominator: int):
        self.numerator: int = numerator
        self.denominator: int = denominator


    def __add__(self, other):
        return Fraction(self.numerator + other.numerator, self.denominator)
    
    def __mul__(self, other):
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

