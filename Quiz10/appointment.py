class Appointment:
    def __init__(self, name: str , hour: int):
        self.mName: str = name
        self.mHour: int = hour


    def display(self) -> str:
        return str(self.mName) + '-' + str(self.mHour)
