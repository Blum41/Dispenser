from .ConnectController import ConnectController
from .DistributionController import DistributionController

import threading


def run_controllers(*args):
    instances = [
        ConnectController(args),
        DistributionController(args),
    ]
    for instance in instances:
        threading.Thread(target=instance).start()
