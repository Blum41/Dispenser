from datetime import datetime, time

from database.Task import Dispensing


class Box:
    def __init__(self, name: int, current_drugs_number: int, rules: dict, initial_number: int):
        assert current_drugs_number >= 0
        self.name: int = name
        self.current_number: int = current_drugs_number
        self.initial_number: int = initial_number
        self.rules = rules
        self.hours = [time(hour=hour["hours"], minute=hour["minutes"]) for hour in self.rules["hours"]]

    def is_not_empty(self, drugs_number: int = 1) -> bool:
        return self.current_number >= drugs_number

    def rule_is_satisfied(self) -> bool:
        return datetime.today().weekday() in self.rules["days"] and time(datetime.now().time().hour, datetime.now().minute) in self.hours

    def get_task(self) -> Dispensing:
        return Dispensing(box=self.name, number=self.rules["quantity"], current_number=self.current_number, initial_number=self.initial_number)
