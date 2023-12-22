from structures.config import Configuration
from structures.grammar import Grammar
from structures.parser_output import ParserOutput


class Parser:
    def __init__(self, grammar: Grammar, word, state='normal') -> None:
        self.grammar = grammar
        self.word = word
        self.state = state
        self.config = Configuration(grammar.start_symbol)

    def momentary_insuccess(self) -> None:
        self.config.current_state = 'back'

    def advance(self) -> None:
        head = self.config.pop_input()

        self.config.push(head)
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
        productions = self.grammar.get_productions_for_nonterminals(top_working_stack[0])
        last_production_index = productions[-1][1]
        if top_working_stack[1] < last_production_index:
            self.another_try1()
        elif self.config.get_current_position() == 1 and top_working_stack[0] == self.grammar.start_symbol:
            self.another_try3()
        else:
            self.another_try2()

    def another_try1(self):
        self.config.current_state = 'normal'
        top_working_stack = self.config.pop()
        non_terminal = top_working_stack[0]
        productions = self.grammar.get_productions_for_nonterminals(non_terminal)
        current_production_length = len(
            [production for production in productions if production[1] == top_working_stack[1]][0][0])
        for i in range(current_production_length):
            self.config.pop_input()
        next_production_input = [production for production in productions if production[1] == top_working_stack[1] + 1][
            0]
        self.config.push_input(next_production_input[0])
        self.config.push((top_working_stack[0], next_production_input[1]))

    def another_try2(self):
        top_working_stack = self.config.pop()
        non_terminal = top_working_stack[0]
        productions = self.grammar.get_productions_for_nonterminals(non_terminal)
        current_production_length = len(
            [production for production in productions if production[1] == top_working_stack[1]][0][0])
        for i in range(current_production_length):
            self.config.pop_input()
        self.config.push_input(non_terminal)

    def another_try3(self):
        self.config.pop_input()
        self.config.pop()
        self.config.current_state = 'error'

    def expand(self):
        top_input_stack = self.config.pop_input()
        production = self.grammar.get_productions_for_nonterminals(top_input_stack)
        first_simple_production = production[0]
        self.config.push((top_input_stack, first_simple_production[1]))
        self.config.push_input(first_simple_production[0])

    def parse(self):
        while self.config.current_state not in ['final', 'error']:
            if self.config.current_state == 'normal':
                if self.config.current_position >= len(self.word) and len(self.config.input) == 0:
                    self.success()
                else:
                    if len(self.config.input) > 0 and self.config.input[0] in self.grammar.nonterminals:
                        print('expand')
                        self.expand()
                    elif self.config.current_position <= len(self.word) and len(self.config.input) > 0 and \
                            self.config.input[0] == self.word[self.config.current_position - 1]:
                        print('advance')
                        self.advance()
                    else:
                        print('mi')
                        self.momentary_insuccess()
            else:
                if self.config.current_state == 'back':
                    if len(self.config.stack) > 0 and ((isinstance(self.config.stack[-1], tuple) and
                                                        self.config.stack[-1][0] in self.grammar.terminals) or (
                                                               isinstance(self.config.stack[-1], str) and
                                                               self.config.stack[-1] in self.grammar.terminals)):
                        print('back')
                        self.back()
                    elif len(self.config.stack) > 0:
                        print('another try')
                        self.another_try()

        if self.config.current_state == 'error':
            print('error')
            return None
        print('sequence accepted')
        print(ParserOutput(self.config).build_string_of_productions())
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
