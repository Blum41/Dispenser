import os
from time import sleep

from flask import Flask, render_template, request, url_for, redirect
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
                self.start_web_server()
            except ConnectError:
                logging.error("Pas internet")
            # sleep(60 * 5)

    def start_web_server(self):
        app = Flask(__name__, template_folder='../templates', static_folder='../templates/static')

        @app.route("/")
        def index():
            return render_template("index.html")

        @app.route("/setup/wifi", methods=["POST", "GET"])
        def setup_wifi():
            print(request.method)
            if request.method == "POST" and request.form.get("wifi"):
                return redirect(url_for("setup_wifi_password", wifi=request.form.get("wifi")))

            wifi_list = self.scan_wifi()
            return render_template("wifi.html", wifi_list=wifi_list)

        @app.route("/setup/wifi/password/<wifi>", methods=["POST", "GET"])
        def setup_wifi_password(wifi):
            if request.method == "POST" and request.form.get("password"):
                return "OUI !" + request.form.get("password")

            return render_template("password.html", wifi=wifi)
        app.run(host="0.0.0.0", port=5000, debug=False)

    def scan_wifi(self):
        result = os.popen("iwlist wlan0 scan | egrep 'ESSID|WPA2|PSK'").read().split("\n")

        wifis = []
        for i in range(len(result)):
            line = result[i].strip()
            if "ESSID" in result[i] and i < len(result) + 1 and "WPA2" in result[i+1] and "PSK" in result[i+2]:
                wifi_name = line.split(":")[1].replace('"', '')
                if wifi_name not in wifis and wifi_name != "":
                    wifis.append(wifi_name)

        return wifis
