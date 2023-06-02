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
                with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
                    content = "ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev"
                    content += "\n"
                    content += "country=FR"
                    content += "\n"
                    content += "\n"
                    content += "network={"
                    content += "\n"
                    content += "\tssid=\"" + str(wifi) + "\""
                    content += "\n"
                    content += "\tpsk=\"" + str(request.form.get("password")) + "\""
                    content += "\n"
                    content += "\tkey_mgmt=WPA-PSK"
                    content += "\n"
                    content += "}"
                    content += "\n"
                    f.write(content)
                    f.close()

                    os.popen("cp /etc/dhcpcd.conf.dynamic /etc/dhcpcd.conf")
                    os.popen("systemctl stop hostapd")
                    os.popen("systemctl unmask hostapd")

                    os.popen("systemctl stop dnsmasq")
                    os.popen("systemctl unmask dnsmasq")
                    os.popen("reboot")

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
