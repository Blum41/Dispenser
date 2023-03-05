import serial


class Arduino:
    def __init__(self, port: str):
        self.ser = serial.Serial(port, 9600)

    def get_value(self, name: str) -> str:
        pass

    def action(self, name: str, value: str):
        pass
