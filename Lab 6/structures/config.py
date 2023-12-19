class Configuration:
    def __init__(self, starting_symbol) -> None:
        self.current_state = 'normal'
        self.current_position = 1
        self.stack = []
        self.input = [[starting_symbol]]

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push_input(self, elem):
        self.input.append(elem)

    def pop_input(self):
        return self.input.pop()

    def increment(self):
        self.current_position += 1

    def decrement(self):
        self.current_position -= 1

    def get_current_state(self):
        return self.current_state

    def set_current_state(self, new_state):
        self.current_state = new_state

    def get_current_position(self):
        return self.current_position

    def get_stack(self):
        return self.stack

    def get_input(self):
        return self.input