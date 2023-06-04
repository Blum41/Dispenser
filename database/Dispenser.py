import json
from os import getenv
import serial

from database.Box import Box
from database.database import Database

from datetime import datetime
from time import sleep


class Dispenser:
    def __init__(self):
        while True:
            try:
                self.serial = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
                self.serial.reset_output_buffer()
                self.serial.reset_input_buffer()
                break
            except:
                pass

        self.is_dispensing: bool = None
        self.boxes: list[Box] = []
        self.database = Database()
        self.drug_is_taken: bool = False
        self.rules = []

    def update(self):
        data = self.database.client.table("dispensers").select("*").eq("id", getenv("DEVICE_ID")).single().execute().data
        boxes = self.database.client.table("boxes").select("*").eq("dispenser_id", getenv("DEVICE_ID")).gt("box_number", 0).gt("current_number", 0).order("box_number", desc=True).execute().data
        self.boxes = []
        for boxe in boxes:
            b = Box(boxe["id"], boxe["box_number"], boxe["current_number"], boxe["rules"], boxe["initial_number"])
            self.boxes.append(b)

    def notify_server(self):
        self.database.client.table("dispensers").update({
            "drug_is_taken": self.drug_is_taken,
            "state_updated_at": datetime.now().isoformat(),
            "boxes_number": len(self.boxes),
            "is_dispensing": self.is_dispensing
        }).eq("id", getenv("DEVICE_ID")).execute()
         
        

    def get_distance(self) -> int:
        """ Return distance in cm """
        self.serial.write("e\n".encode("utf-8"));

        while True:
            data = self.serial.readline().decode("utf-8")
            if "distance=" in data:
                sleep(0.1)
                return int(data.split("=")[1])

    def switch_is_on(self) -> bool:
        self.serial.write("e\n".encode("utf-8"));
        while True:
            data = self.serial.readline().decode("utf-8")
            if "switch1=" in data:
                sleep(0.1)
                return int(data.split("=")[1]) == 1
    
    def led_on(self, number: int):
        self.serial.write(f"L{number}=1\n".encode("utf-8"))
        
    def led_off(self, number: int):
        self.serial.write(f"L{number}=0\n".encode("utf-8"))

    def set_servo_position(self, number: int, angle: int) -> None:
        """ Set servo position with given angle in degrees"""
        self.serial.write(f"S{number}={angle}\n".encode("utf-8"))
        sleep(2)
