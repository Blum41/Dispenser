class State:
    def __init__(self, name: str, color, animation: int, priority: int):
        self.color = Color()
        self.name = name
        self.priority = priority

    def __eq__(self, other):
        return self.name == other.name
