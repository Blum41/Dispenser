from RPi import GPIO

from electronics.Arduino import Arduino


class Component:
    def __init__(self, name: str):
        self.name = name


class Sensor(Component):
    def __init__(self, name: str, arduino: Arduino):
        super().__init__(name)
        self.arduino = arduino
        self.value = None

    def get_value(self):
        return self.value

    def update_value(self):
        pass


class Switch(Component):
    def __init__(self, name: str):
        super().__init__(name)
        self.state = False

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def is_on(self):
        return self.state

    def switch(self):
        if self.state:
            self.turn_off()
        else:
            self.turn_on()


class GpioSwitch(Switch):
    def __init__(self, name: str, pin: int):
        super().__init__(name)
        assert isinstance(pin, int)
        assert 1 <= pin <= 27 and pin not in [1, 2, 3, 10, 11, 14, 15]
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):
        super().turn_on()
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        super().turn_off()
        GPIO.output(self.pin, GPIO.LOW)
