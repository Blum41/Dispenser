import RPi.GPIO as GPIO
from dotenv import load_dotenv

from controllers import run_controllers
from database.Dispenser import Dispenser
from electronics.ComponentCollection import ComponentCollection


def run():
    print("Client started")
    load_dotenv()

    GPIO.setmode(GPIO.BCM)

    component_collection = ComponentCollection([])
    dispenser = Dispenser(component_collection)

    run_controllers(dispenser)


if __name__ == "__main__":
    run()
