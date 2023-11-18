from appointment import Appointment


class Lunch(Appointment):
    def __init__(self, name: str):
        super().__init__(name, 12)
