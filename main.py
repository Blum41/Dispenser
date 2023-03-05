from RPi import GPIO

from controllers import run_controllers
from dispenser.Dispenser import Dispenser
from electronics.ComponentCollection import ComponentCollection


def run():
    print("Client started")

    GPIO.setmode(GPIO.BCM)

    component_collection = ComponentCollection([])
    dispenser = Dispenser(component_collection)

    run_controllers(dispenser)


if __name__ == "__main__":
    run()
