import os
from time import sleep

from httpcore import ConnectError

from database.Dispenser import Dispenser
import logging


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
                logging.error("Pas internet")
            # sleep(60 * 5)
