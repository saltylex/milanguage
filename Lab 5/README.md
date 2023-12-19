#### Grammar
The grammar used for the parser is implemented using arrays and objects.

#### Class attributes
- nonterminals: the non-terminals of the grammar
- terminals: the terminals of the grammar
- productions: the productions of the grammar
- start_symbol: the start symbol of the grammar

####Operations
- read(filename): reads the grammar from a file
- is_CFG(): checks if the grammar is context free
- get_productions_for_nonterminals(nonterminal):  returns the productions for a given non-terminal
- export(): to string