from datetime import datetime

from database.Dispenser import Dispenser


class Dispensing:
    def __init__(self, box: int, number: int):
        assert number > 0, "number must be highter than 0"
        self.box = box
        self.number = number

    def dispense(self, dispenser: Dispenser):
        print("DISTRIBUTION EN COURS !!!!!!!!!!!!")
