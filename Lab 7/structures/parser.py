from structures.config import Configuration
from structures.grammar import Grammar


class Parser:
    def __init__(self, grammar: Grammar, word, state='q') -> None:
        self.grammar = grammar
        self.word = word
        self.state = state
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

    def parse(self, word: list):
        while self.config.current_state not in ['f', 'e']:
            if self.config.current_state == 'q':
                if self.config.current_position == len(word) + 1 and len(self.config.input) == 0:
                    self.success()
                else:
                    if len(self.config.input) > 0 and self.config.input[-1] in self.grammar.nonterminals:
                        self.expand()
                    elif self.config.current_position < len(word) and len(self.config.input) > 0 and self.config.input[
                        -1] == word[self.config.current_position - 1]:
                        self.advance()
                    else:
                        self.momentary_insuccess()
            else:
                if self.config.current_state == 'b':
                    if len(self.config.stack) > 0 and self.config.stack[-1] in self.grammar.terminals:
                        self.back()
                    elif len(self.config.stack) > 0:
                        self.another_try()

        if self.config.current_state == 'e':
            print('error')
            return None
        print('sequence accepted')
        return self.config.stack

    def get_tree(self, production_string):
        if not production_string:
            return []
        result = [(production_string[0].split('|')[0], -1, -1)]
        i = 0
        j = 0
        while j < len(production_string) and i < len(result):
            top = result[i]
            if top[0] not in self.grammar.nonterminals:
                i += 1
                continue
            expand_with = None
            while j < len(production_string):
                if '|' not in production_string[j]:
                    j += 1
                    continue
                non_terminal, production_number = production_string[j].split('#')
                if non_terminal == top[0]:
                    expand_with = (non_terminal, production_number)
                    j += 1
                    break
                j += 1
            if j == len(production_string):
                break
            non_terminal, production_number = expand_with
            production_number = int(production_number)
            production = self.grammar.get_productions_for_nonterminals(non_terminal)[production_number][1].split()
            added = 1
            for symbol in production:
                result.insert(i + added, (symbol, i, i + 1 + added))
                added += 1
            result[i + added - 1] = (*result[i + added - 1][:-1], -1)
            i += 1
        return result
