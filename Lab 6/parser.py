from structures.config import Configuration
from structures.grammar import Grammar


class Parser:
    def __init__(self, grammar: Grammar, word) -> None:
        self.grammar = grammar
        self.word = word
        self.config = Configuration(grammar.start_symbol)

    def momentary_insuccess(self) -> None:
        self.config.current_state = 'back'

    def advance(self) -> None:
        head = self.config.pop_input()
        terminal = head[0]

        if len(head) > 1:
            self.config.push_input(head[1:])

        self.config.push(terminal)
        self.config.increment()

    def back(self) -> None:
        self.config.decrement()
        head = self.config.pop()
        self.config.push_input([head])

    def success(self) -> None:
        self.config.current_state = 'final'

    def get_config(self):
        return self.config

    def another_try(self):
        top_working_stack = self.config.peek()
        if len(top_working_stack) > 1:
            self.another_try1()
        elif self.config.get_current_position == 1 and top_working_stack == self.grammar.start_symbol:
            self.another_try3()
        else:
            self.another_try2()

    def another_try1(self):
        self.config.current_state = 'normal'
        self.config.pop_input()
        top_working_stack = self.config.pop()
        next_simple_production = top_working_stack[0]
        self.config.push(next_simple_production)
        self.config.push_input(next_simple_production[0])

    def another_try2(self):
        self.config.pop_input()
        top_working_stack = self.config.pop()
        top_working_stack_parent = top_working_stack[0]
        self.config.push_input([top_working_stack_parent])

    def another_try3(self):
        self.config.pop_input()
        self.config.pop()
        self.config.current_state = 'error'

    def expand(self):
        top_input_stack = self.config.pop_input()
        non_terminal = top_input_stack[0]
        if len(top_input_stack) > 1:
            self.config.push_input(top_input_stack[1:])
        production = self.grammar.get_productions_for_nonterminals(non_terminal)
        first_simple_production = production[0]
        self.config.push(first_simple_production)
        self.config.push_input(first_simple_production[0])