from electronics.components import Component


class ComponentCollection:
    def __init__(self, components: list[Component]):
        self.components = components

    def add_component(self, component: Component):
        self.components.append(component)

    def get_by_object(self, name: str, object_type: type):
        for component in self.components:
            if isinstance(component, object_type) and component.name == name:
                return component
        return None
