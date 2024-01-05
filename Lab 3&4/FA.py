class FiniteAutomata:

    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initial = None
        self.finals = []
        self.transitions = {}

    def read_from_file(self, file_path):
        # reinitializing values
        self.states = []
        self.alphabet = []
        self.initial = None
        self.finals = []
        self.transitions = {}

        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.replace('\n', "").strip() for line in lines]

            self.states = lines[0].split(" ")
            self.alphabet = lines[1].split(" ")
            self.initial = lines[2]
            self.finals = lines[3].split(" ")
            for index in range(4, len(lines)):
                # read a transition
                trans = lines[index].split(" ")
                initial = trans[0]
                route = trans[1]
                final = trans[2]

                if (initial, route) in self.transitions.keys():
                    # checking if we have multiple final states
                    self.transitions[(initial, route)].append(final)
                else:
                    self.transitions[(initial, route)] = [final]

        return self.validate()

    def validate(self):
        # validate initial state
        if self.initial not in self.states:
            return False, "The initial state must be among the states"
        # validate final states
        for final in self.finals:
            if final not in self.states:
                return False, "All final states must be among the states"

        # validate transitions
        for tr in self.transitions.keys():
            if tr[0] not in self.states or tr[1] not in self.alphabet:
                print(tr[0], tr[1])
                return False, "Transitions must be in the form (state, alphabet element, state)"
            for finalState in self.transitions[tr]:
                if finalState not in self.states:
                    print(finalState)
                    return False, "Transitions must be in the form (state, alphabet element, state)"

        # states and alphabet don't intersect
        for state in self.states:
            if state in self.alphabet:
                return False, "States and alphabet must not overlap"

        return True, ""

    def is_dfa(self):
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return False
        return True

    def is_sequence_accepted(self, sequence):
        if not self.is_dfa():
            return False
        state = self.initial
        for symbol in sequence:
            if (state, symbol) in self.transitions.keys():
                state = self.transitions[(state, symbol)][0]
            else:
                return False
        return state in self.finals

    def get_states(self):
        return self.states

    def get_alphabet(self):
        return self.alphabet

    def get_initial(self):
        return self.initial

    def get_final_states(self):
        return self.finals

    def get_transitions(self):
        return self.transitions
