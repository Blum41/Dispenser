from abc import ABC, abstractmethod
from datetime import time, datetime

from database import Task
from database.Task import Dispensing


class Rule(ABC):
    @abstractmethod
    def is_satisfied(self) -> bool:
        pass

    def get_task(self) -> Dispensing:
        return Dispensing(box=1, number=1)


class WeeklyRule(Rule):
    def __init__(self, days_of_week: list, hours: list[time]):
        self.days_of_week = days_of_week
        self.hours = hours

    def is_satisfied(self) -> bool:
        return datetime.today().weekday() in self.days_of_week and datetime.now().time() in self.hours


class EveryHour(Rule):
    def __init__(self, hours: int):
        self.hours = hours

    def is_satisfied(self) -> bool:
        pass

