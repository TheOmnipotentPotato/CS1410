#Contains Pen Class and Mehtods

class Pen:
    def __init__(self):
        self.mInk: int = 5

    def write(self):
        self.mInk -= 1

    def refill(self):
        self.mInk = 5

    def check_ink(self):
        status: str = ""
        ink_buffer: int = self.mInk
        for i in range(0,5):
            #rather nasty one line solution to the string concat
            #it could be more elegantly written but I think this
            #minimizes the number of control flow branches to be
            #checked at runtime, not that performace is a big issue
            status += ("#"*(ink_buffer>0) or ".")
            ink_buffer -= 1
        return "[" + status + "]"

