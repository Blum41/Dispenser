import os

from flask import Flask, render_template

from tools.network_manager import is_connected


class ConnectController:
    """ Connect to internet """

    def __init__(self, dispenser):
        self.dispenser = dispenser

    def __call__(self):
        # if is_connected():
        #     print("Connected")
        #     # self.run_web()
        # else:
        #     print("Not connected")
        pass


    def run_web(self):
        app = Flask(__name__, template_folder='../templates')

        @app.route("/")
        def index():

            return render_template("index.html")

        app.run(host='0.0.0.0', port=5000, debug=True)
