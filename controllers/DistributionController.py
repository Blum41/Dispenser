import datetime
import threading

from database import Task


class DistributionController:
    def __init__(self, dispenser):
        self.dispenser = dispenser[0]
        self.tasks: list[Task] = []

    def __call__(self):
        threading.Thread(target=self.update_tasks).start()
        threading.Thread(target=self.dispensing).start()

    def update_tasks(self):
        current_time = datetime.datetime.now()
        hour, minute = current_time.hour, current_time.minute

        while True:
            while datetime.datetime.now().hour == hour and datetime.datetime.now().minute == minute:
                pass
            hour, minute = datetime.datetime.now().hour, datetime.datetime.now().minute

            for box in self.dispenser.boxes:
                if box.rule_is_satisfied():
                    self.tasks.append(box.get_task())

    def dispensing(self):
        while True:
            if len(self.tasks) > 0:
                task = self.tasks.pop(0)
                task.dispense(self.dispenser)

    def update_dispenser(self):
        self.update_dispenser()
