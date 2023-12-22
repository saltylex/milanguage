Scanner
The Scanner is implemented.

Regex
The following regexes are used to match the tokens:

identifier: ^[a-zA-Z][a-zA-Z0-9]*$
constant: ^\"[A-Za-z0-9\.\?\!, ]*\"$ (strings) and ^-?[1-9][0-9]*$ (integers)
Finite Automata
The finite automata parser is implemented using arrays and objects. It is used to match the following tokens:

integer constants (fa_id.in)
identifiers (fa_id.in)
Class attributes
states -> the number of states in the finite automata
alphabet -> the alphabet of the finite automata
transitions -> the transition function of the finite automata
initial_state -> the initial state of the finite automata
final_states -> the final states of the finite automata
err -> error string used to signal that the finite automata is in an invalid state
Operations
read(filename) -> reads the finite automata from a file
validate() -> validates the finite automata
is_deterministic() -> checks if the finite automata is deterministic
is_accepted(sequence) -> checks if a given sequence is accepted by the finite automata
getters for the class attributes
Structure
The finite automata is read from an input file with the following structure:

file = states '\n' alphabet '\n' initial_state '\n' final_states '\n' transitions
states = state {' ' state}
alphabet = symbol {' ' symbol}
initial_state = state
final_state = state {' ' state}
transitions = transition {'\n' transition}
transition = state ' ' symbol ' ' state
state = letter {digit}
symbol = letter | digit | special
letter = 'a' | 'b' | ... | 'z' | 'A' | 'B' | ... | 'Z'
digit = '0' | '1' | ... | '9'
special = '+' | '-' | '_' | ...  
Grammar
The grammar used for the parser is implemented using arrays and objects.

Class attributes
non_terminals -> the non-terminals of the grammar
terminals -> the terminals of the grammar
productions -> the productions of the grammar
start_symbol -> the start symbol of the grammar
Operations
read(filename) -> reads the grammar from a file
is_CFG() -> checks if the grammar is context free
getters for the class attributes
get_productions_for_nonterminals(nonterminal) -> returns the productions for a given non-terminal
export()
Parser
The parser implements the functionality of a Recursive Descendent parsing algorithm using a table to represent the Parsing Tree.

Class Atrributes
grammar -> the grammar used
word -> the sequence to parse
config -> the configuration used
The Configuration class represents the stacks and members used by the parser, along with methods to use said stacks and members

stack -> the work stack
input -> the input stack
current_state -> the current state of the parser
current_position -> the current position in the work stack
Operations
momentary_insuccess -> sets the state to a backtracking state
success -> sets the state to a successful state
advance -> parses through one character in the work stack
back -> goes back a character that was parsed
expand -> expands the used grammar to continue parsing
another_try -> goes back and uses another approach to advance by expanding