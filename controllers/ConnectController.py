import os
from time import sleep

from httpcore import ConnectError

from database.Dispenser import Dispenser


class ConnectController:
    """ Connect to internet """

    def __init__(self, dispenser):
        self.dispenser: Dispenser = dispenser[0]

    def __call__(self):
        while True:
            try:
                self.dispenser.update()
                self.dispenser.notify_server()
            except ConnectError:
                print("Pas internet")
            sleep(60 * 5)
