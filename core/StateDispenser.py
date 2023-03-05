class StateDispenser:
    def __init__(self, states):
        self.states = states
        self.current_states = []

    def change_state(self, state_name: str):
        self.current_states.append(self.states.find(state))
        for state in self.current_states:
            if state.name == state_name:
                self.current_states.append(state)
                break

        self.current_states.sort(key=lambda state: state.priority)

    def current_state(self):
        if len(self.current_states) > 0:
            return self.current_states[-1]
        return None

    def remove_state(self, state_name: str):
        for state in self.current_states:
            if state.name == state_name:
                self.current_states.remove(state)
                break
