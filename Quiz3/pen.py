

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
            status += ("#"*(ink_buffer>0) or ".")
            ink_buffer -= 1
        return "[" + status + "]"

