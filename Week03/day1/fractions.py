class Fraction:

    def __init__(self, numerator, denominator):
        for i in range(2, min(numerator, denominator)):
            print(int(numerator // i), i)
            print(numerator / i, i)

            if numerator // i == int(numerator / i):
                if denominator // i == int(denominator / i):
                    numerator = int(numerator//i)
                    denominator = int(denominator/i)
                    print("boo", i, numerator, denominator)

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __add__(self, other):
        new_nom = self.numerator * other.denominator + self.denominator* other.numerator
        new_denom = self.denominator * self.denominator 
        return Fraction(new_nom, new_denom)

    def __sub__(self, other):
        new_nom = self.numerator * other.denominator - self.denominator* other.numerator
        new_denom = self.denominator * self.denominator 
        return Fraction(new_nom, new_denom)

    def __mul__(self, other):
        new_nom = self.numerator * other.numerator
        new_denom = self.denominator * self.denominator 
        return Fraction(new_nom, new_denom)

    def __truediv__(self, other):
        new_nom = self.numerator * other.denominator
        new_denom = self.denominator * self.numerator
        return Fraction(new_nom, new_denom)




a = Fraction(1, 2)
b = Fraction(2, 4)

print(a)
print(b)
print(a == b) # True

print(a + b) # 1
print(a - b) # 0
print(a * b) # 1 / 4
print(a / b)