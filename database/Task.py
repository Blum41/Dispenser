from datetime import datetime
from time import sleep


class Dispensing:
    def __init__(self, box: int, number: int, initial_number: int, current_number: int):
        assert number > 0, "number must be highter than 0"
        self.box = box
        self.number = number
        self.initial_number = initial_number
        self.current_number = current_number

    def dispense(self, dispenser):
        
        for i in range(self.number):
            print("a")
            angle = 20 * (self.initial_number - (self.current_number - i) + 1)

            dispenser.set_servo_position(self.box, angle)
            print("b")
            sleep(1.5)
            
