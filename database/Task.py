from datetime import datetime
from time import sleep

from database.database import Database


class Dispensing:
    def __init__(self, box_o, box: int, number: int, initial_number: int, current_number: int):
        assert number > 0, "number must be highter than 0"
        self.box = box
        self.box_o = box_o
        self.number = number
        self.initial_number = initial_number
        self.current_number = current_number
        self.database = Database()
        
    def dispense(self, dispenser):
        
        for i in range(self.number):
            angle = 20 * (self.initial_number - (self.current_number - i) + 1)

            if 0 <= angle <= 180:
                dispenser.set_servo_position(self.box, angle)
                sleep(1.5)
                self.box_o.current_number -= 1
        
        
        self.database.client.table("boxes").update({
            "current_number": self.box_o.current_number
        }).eq("id", self.box_o.id).execute()
