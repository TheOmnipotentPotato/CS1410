from fraction import Fraction


if __name__== "__main__":
    f1 = Fraction(2,4)
    f2 = Fraction(1,4)

    f3 = f1 + f2

    f4 = f1 * f2
    print(str(f3))
    print(str(f4))

    print("using __repr__ rather than print(__str__)")

    print(f3)
    print(f4)

