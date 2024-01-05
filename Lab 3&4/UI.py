from FA import FiniteAutomata


class UI:

    def __init__(self) -> None:
        self.__cmds = {
            '1': self.read_FA_given_file,
            '2': self.printStates,
            '3': self.printAlphabet,
            '4': self.printTransitions,
            '5': self.printFinalStates,
            '6': self.printInitialState,
            '7': self.verifyDFA,
            '8': self.verifySequence
        }
        self.fa = FiniteAutomata()
        self.read_FA('FA.in')

    @staticmethod
    def show_menu():
        print("\n1.Read FA from file")
        print("2.Display FA States")
        print("3.Display FA Alphabet")
        print("4.Display FA transitions")
        print("5.Display FA final states")
        print("6.Display FA initial state")
        print("7.Verify if FA is DFA")
        print("8.verify if a sequence is accepted by the FA\n")

    def run(self):
        self.show_menu()
        while True:
            # self.show_menu()
            cmd = input(" > ")
            if cmd in self.__cmds.keys():
                self.__cmds[cmd]()
            elif cmd == "x":
                return
            elif cmd == 'm':
                self.show_menu()
            else:
                print("Invalid option")
                continue

    def read_FA(self, file):
        (isValid, msg) = self.fa.read_from_file(file)
        if not isValid:
            print("The FA is invalid")
            print("  > " + msg)
            return

    def read_FA_given_file(self):
        file = input("Input file name: ")
        self.read_FA(file)

    def printStates(self):
        print("  States: ")
        print(self.fa.get_states())

    def printAlphabet(self):
        print("  Alphabet")
        print(self.fa.get_alphabet())

    def printTransitions(self):
        print("  Transitions")
        transitions = self.fa.get_transitions()
        for t in transitions.keys():
            src = str(t[0])
            route = str(t[1])
            for d in transitions[t]:
                dest = str(d)
                print(" (" + src + "," + route + ") -> " + dest)

    def printFinalStates(self):
        print("  Final states")
        print(self.fa.get_final_states())

    def printInitialState(self):
        print("  Initial state: " + str(self.fa.get_initial()))

    def verifyDFA(self):
        if self.fa.is_dfa():
            print("It is DFA")
        else:
            print("It is not DFA")

    def verifySequence(self):
        if self.fa.is_dfa():
            seq = input(" >> Sequence: ")
            if self.fa.is_sequence_accepted(seq):
                print("Accepted")
            else:
                print("Not accepted")
        else:
            print("Your FA is not deterministic")
