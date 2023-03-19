from electronics.ComponentCollection import ComponentCollection


class Dispenser:
    def __init__(self, component_collection: ComponentCollection):
        self.component_collection = component_collection
        self.in_distribution = False
