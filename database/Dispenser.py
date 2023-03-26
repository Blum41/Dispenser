from os import getenv

from database.Rule import Rule
from database.database import Database
from electronics.ComponentCollection import ComponentCollection

from datetime import datetime


class Dispenser:
    def __init__(self, component_collection: ComponentCollection):
        self.is_dispensing: bool = None
        self.boxes = []
        self.database = Database()
        self.component_collection = component_collection
        self.drug_is_taken: bool = False
        self.rules: list[Rule] = []

    def update(self):
        data = self.database.client.table("dispensers").select("*").eq("id", getenv("DEVICE_ID")).single().execute().data
        data_2 = self.database.client.table("boxes").select("*").eq("dispenser_id", getenv("DEVICE_ID")).execute()
        print(data_2)

    def notify_server(self):
        self.database.client.table("dispensers").update({
            "drug_is_taken": self.drug_is_taken,
            "state_updated_at": datetime.now().isoformat(),
            "boxes_number": len(self.boxes),
            "is_dispensing": self.is_dispensing
        }).eq("id", getenv("DEVICE_ID")).execute()
