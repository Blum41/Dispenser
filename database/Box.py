class Box:
    def __init__(self, name: str, current_drugs_number: int):
        assert current_drugs_number >= 0
        self.name: str = name
        self.current_number: int = current_drugs_number

    def is_not_empty(self, drugs_number: int = 1) -> bool:
        return self.current_number >= drugs_number
