from datetime import datetime, time

from database.Task import Dispensing


class Box:
    def __init__(self, name: int, current_drugs_number: int, rule: dict):
        assert current_drugs_number >= 0
        self.name: int = name
        self.current_number: int = current_drugs_number
        self.rule = rule
        self.hours = [time(hour=hour["hour"], minute=hour["minute"]) for hour in self.rule["hours"]]

    def is_not_empty(self, drugs_number: int = 1) -> bool:
        return self.current_number >= drugs_number

    def rule_is_satisfied(self) -> bool:
        return datetime.today().weekday() in self.rule["days"] and time(datetime.now().time().hour, datetime.now().minute) in self.hours

    def get_task(self) -> Dispensing:
        return Dispensing(box=1, number=self.rule["quantity"])
