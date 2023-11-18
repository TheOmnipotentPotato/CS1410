from appointment import Appointment

class Doctor(Appointment):
    def __init__(self, hour: int):
        super().__init__("Doctor", hour)
