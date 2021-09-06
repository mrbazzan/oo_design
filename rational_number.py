
class Rational:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __float__(self):
        return float(self.numerator/self.denominator)

    def __add__(self, other):
        up = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        down = (self.denominator * other.denominator)
        return self.__class__(up, down)

    def __mul__(self, other):
        up = (self.numerator * other.numerator)
        down = (self.denominator * other.denominator)
        return self.__class__(up, down)

    @staticmethod
    def _gcd(a, b):
        while a != b:
            if a < b:
                a, b = b, a
            if a > b:
                a -= b
        return a

    def _reduce(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcd)
        self.denominator = int(self.denominator / gcd)
