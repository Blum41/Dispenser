class Color:
    """ Class to represent a color """

    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0

    def set_by_rgb(self, red: int, green: int, blue: int):
        """ Define the color from RGB values """
        assert 0 <= red <= 255
        assert 0 <= green <= 255
        assert 0 <= blue <= 255

        self.red = red
        self.green = green
        self.blue = blue

    def set_by_hexadecimal(self, hex: str):
        """ Define the color from a hexadecimal value """
        assert len(hex) == 6

        self.red = int(hex[1:3], 16)
        self.green = int(hex[3:5], 16)
        self.blue = int(hex[5:7], 16)

    def __str__(self):
        return f"# {self.red:02x}{self.green:02x}{self.blue:02x}"

    def __repr__(self):
        return f"Color : ({self.red}, {self.green}, {self.blue})"
