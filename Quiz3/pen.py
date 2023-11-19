#Contains Pen Class and Mehtods

class Pen:
    def __init__(self):
        self.mInk: int = 5

    def write(self):
        if self.mInk > 0:
            self.mInk -= 1
        else:
            print("The pen is empty, please fill it")

    def refill(self):
        self.mInk = 5

    def check_ink(self):
        return "[" + "#"*self.mInk + "."*(5-self.mInk) + "]"

