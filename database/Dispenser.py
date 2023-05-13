import json
from os import getenv
import serial

from database.Box import Box
from database.Rule import Rule
from database.database import Database
from electronics.ComponentCollection import ComponentCollection

from datetime import datetime
from time import sleep


class Dispenser:
    def __init__(self, component_collection: ComponentCollection):
        self.serial = serial.Serial("/dev/ttyACM0", 9600, timeout=3.0)
        self.serial.reset_output_buffer()
        self.serial.reset_input_buffer()

        self.is_dispensing: bool = None
        self.boxes: list[Box] = []
        self.database = Database()
        self.component_collection = component_collection
        self.drug_is_taken: bool = False
        self.rules = []

    def update(self):
        data = self.database.client.table("dispensers").select("*").eq("id", getenv("DEVICE_ID")).single().execute().data
        boxes = self.database.client.table("boxes").select("*").eq("dispenser_id", getenv("DEVICE_ID")).gt("boxes_number", 0).order("boxes_number", desc=True).execute().data
        self.boxes = []
        for boxe in boxes:
            b = Box(boxe["boxes_number"], boxe["current_drugs_number"], boxe["rule"])
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
        while True:
            data = self.serial.readline().decode("utf-8")
            if "distance=" in data:
                sleep(0.1)
                return int(data.split("=")[1])

    def set_servo_position(self, number: int, angle: int) -> None:
        """ Set servo position with given angle in degrees"""
        self.serial.write(f"S{number}={angle}\n".encode("utf-8"))
        sleep(2)
