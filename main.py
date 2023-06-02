from time import sleep

import RPi.GPIO as GPIO
from dotenv import load_dotenv
from flask import render_template, Flask

from controllers import run_controllers
from database.Dispenser import Dispenser

import logging
import os

def run():
    logging.log(logging.INFO, "Starting dispenser")
    load_dotenv()

    GPIO.setmode(GPIO.BCM)
    sleep(2)
    dispenser = Dispenser()
    # print(os.popen("iwlist wlan0 scan | egrep 'ESSID|WPA2'").read().replace(" ", "").split("\n"))
    sleep(2)
    # def scan_wifi():
    #     result = os.popen("iwlist wlan0 scan | egrep 'ESSID|WPA2|PSK'").read().replace(" ", "").split("\n")
    #
    #     wifis = []
    #     for i in range(len(result)):
    #         if "ESSID" in result[i] and i < len(result) + 1 and "WPA2" in result[i+1] and "PSK" in result[i+2]:
    #             wifi_name = result[i].split(":")[1].replace('"', '')
    #             if wifi_name not in wifis and wifi_name != "":
    #                 wifis.append(wifi_name)
    #     return wifis
    logging.log(logging.INFO, "Success start")

    run_controllers(dispenser)


if __name__ == "__main__":
    run()
