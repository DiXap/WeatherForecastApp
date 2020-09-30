from state import State

class States(object):
    """
    docstring
    """
    def __init__(self) -> None:
        self.states = {}
        self.cities = []

    def add(self, state: State):
        """
        docstring
        """
        self.states[state][state.cities]