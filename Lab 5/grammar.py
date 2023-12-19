class Grammar:
    def __init__(self) -> None:
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.start_symbol = None

    def read(self, filename) -> None:
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.start_symbol = None

        with open(filename, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\n', "").strip() for line in lines]

            self.nonterminals = lines[0].split(" ")
            self.terminals = lines[1].split(" ")
            self.start_symbol = lines[2]

            production_index = 0
            for index in range(3, len(lines)):
                production = lines[index]
                l, r = production.split("->")
                l = l.strip().split(' ')
                r = r.strip().split(' ')
                l = tuple(l)

                for val in r:
                    production_index += 1
                    values = val.strip().split(' ')

                    if l in self.productions.keys():
                        self.productions[l].append((values, production_index))
                    else:
                        self.productions[l] = [(values, production_index)]

    def get_terminals(self):
        return self.terminals

    def get_nonterminals(self):
        return self.nonterminals

    def get_productions(self):
        return self.productions

    def get_productions_for_nonterminals(self, nonterminal):
        productions = []

        if self.is_CFG():
            for l in self.productions.keys():
                if l[0] == nonterminal:
                    return self.productions[l]

        return productions

    def is_CFG(self) -> bool:
        for l in self.productions.keys():
            if len(l) != 1:
                return False
            if l[0] not in self.nonterminals:
                return False
        return True

    def export(self) -> None:
        print("Terminals:")
        print(self.terminals)
        print("Nonterminals:")
        print(self.nonterminals)
        print("Productions:")
        for i in self.productions.keys():
            print(str(i) + ' -> ' + str(self.productions[i]))
