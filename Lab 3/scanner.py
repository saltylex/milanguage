import re

from PIF import PIF
from symboltable import SymbolTable
from utils import read_tokens, read_program


class Scanner:

    def __init__(self):
        self.operators, self.separators, self.keywords = read_tokens("token.in")

        self.identifiersTable = SymbolTable(100)
        self.constantsTable = SymbolTable(100)
        self.pif = PIF()

        self.errors = []

    def is_reserved(self, token):
        return token in self.keywords

    def is_operator(self, token):
        return token in self.operators

    def is_separator(self, token):
        return token in self.separators

    def is_token(self, token):
        return self.is_reserved(token) or self.is_operator(token) or self.is_separator(token)

    @staticmethod
    def is_identifier(token):
        return re.match("^[a-z][\w]*$", token) is not None

    def is_const(self, token):
        return self.is_number(token) or self.is_string(token)

    @staticmethod
    def is_number(token):
        return token == "0" or re.match("^-?[1-9][0-9]*$", token) is not None

    @staticmethod
    def is_string(token):
        return re.match("^\"[A-Za-z0-9\.\?\!\-, ]*\"$", token) is not None

    def tokenize(self, line):
        # remove spaces and newlines
        line = line.replace('\n', '').strip()

        if line == '':
            return []

        # handle the strings and the operators
        line, strings = self.search_for_strings(line)
        line = self.search_for_operators(line)

        # split the line by the separators
        for separator in self.separators:
            line = line.replace(separator, " " + separator + " ")
        tokens = line.split(" ")
        tokens = [t for t in tokens if t != '']

        # replace back the string tokens
        for i in range(len(tokens)):
            if re.match("^\$[0-9]+\$$", tokens[i]) is not None:
                tokens[i] = strings[int(tokens[i][1:-1])]

        return tokens

    def search_for_operators(self, line):
        result = ""
        i = 0
        while i < len(line):
            # check for compound operators
            if i + 1 < len(line) and self.is_operator(line[i] + line[i + 1]):
                result += " " + line[i] + line[i + 1] + " "
                i += 1
            # check for simple operators
            elif self.is_operator(line[i]):
                result += " " + line[i] + " "
            else:
                result += line[i]
            i += 1
        return result

    @staticmethod
    def search_for_strings(line):
        # replace the strings ("...") with $id$, where id is the index in the list of strings
        strings = []
        line_without_strings = ""

        i = 0
        is_string = False
        string = ""

        while i < len(line):

            # when encountering a '"', its either the beginning or end of a string
            if line[i] == '"':
                # we add the finished string to the list as $index$
                if is_string:
                    string += '\"'
                    strings.append(string)
                    line_without_strings += " $" + str(len(strings) - 1) + "$ "
                # otherwise, we start a new string
                else:
                    string = '\"'
                is_string = not is_string

            else:
                if is_string:
                    string += line[i]
                else:
                    line_without_strings += line[i]
            i += 1

        if is_string:
            strings.append(string)
            line_without_strings += " $" + str(len(strings) - 1) + "$ "

        return line_without_strings, strings

    def error(self, token, line_no):
        self.errors.append("Lexical error at line " + str(line_no) + ": " + token)

    def output(self):
        with open("PIF.out", 'w') as file:
            file.write(str(self.pif))
        with open("ST.out", 'w') as file:
            file.write("Identifiers:\n\n")
            file.write(str(self.identifiersTable))
            file.write("\n")
            file.write("Constants:\n\n")
            file.write(str(self.constantsTable))

    def scan(self, file_path):
        # read the program and initialize line number
        program = read_program(file_path)
        line_number = 0

        for line in program:
            # detect tokens
            line_number += 1
            tokens = self.tokenize(line)

            for token in tokens:
                if self.is_reserved(token) or self.is_operator(token) or self.is_separator(token):
                    self.pif.add(token, (-1, -1))
                else:
                    if self.is_identifier(token):
                        index = self.identifiersTable.add(token)
                        self.pif.add("id", index)
                    elif self.is_const(token):
                        index = self.constantsTable.add(token)
                        self.pif.add("constant", index)
                    else:
                        self.error(token, line_number)

        # handle errors
        if len(self.errors) == 0:
            print("Lexically correct")
            self.output()
        else:
            print("Error!")
            for err in self.errors:
                print(err)
