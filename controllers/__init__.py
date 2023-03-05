from .ConnectController import ConnectController
from .DistributionController import DistributionController


def run_controllers(*args):
    instances = [
        ConnectController(args),
        DistributionController(args),
    ]
    while True:
        for instance in instances:
            instance()
