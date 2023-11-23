### Milanguage

**Github Repository: https://github.com/saltylex/milanguage**

**Student: Goia Alexia Maria, 933/1**

This is a documentation of the implementation in Python of Milanguage, a C++ based programming language.

#### Symbol Table

The symbol table uses two hashtables, separate for identifiers and constants (two instances).

##### Structure

The elements of the hashtable are represented as a main list with a given size, where the positions represent the hashed values of the keys. Collisions are solved using separate chaining, on each position we are placing the elements using the deque from Python.

**Class Attributes:**
- size (given as parameter)
- number of elements
- elements

**Operations:**
- add(key) - adds a new symbol in the table
- get_position(key) - for given symbol returns the position as a tuple (index, position) 
- exists(key) - checks if a symbol is in the table or not 
- size() — returns the number of symbols currently in the symbol table 

When adding a new symbol, the hash value corresponding to the symbol is computed and the element is added at the computed position in the list; if there are more elements on that position, the new element is added at the end of the corresponding deque. If the same symbol already exists in the symbol table, it is not added again. 

The hash value is computed using the sum of the ASCII codes of the string corresponding to it, returning it modulo the size of the table.

#### Program internal form (PIF)

##### Structure
The PIF is implemented as a list of tuples, containing the token and the location.
- if the token is an operator/separator/keyword it appears as is, with the location (-1,-1)
- if token is an id/constant, "id"/"constant" appear together with the actual location in the symbol table.

**Operations:**
- add(token, index): adds the tuple to the list of elements
- (utils.py) readTokens(file): reads operators/separators/keywords from token.in
- (utils.py) readProgram(file): reads given program and returns a list of the lines.

#### Scanner
The scanner is responsible of tokenizing, scanning and providing the output.

##### Attributes:
- operators, separators, keywords: read from the tokens file
- identifiersTable: symbol table containing only identifiers
- constantsTable: symbol table containing only constants
- pif: instance of Program internal form class
- errors: keeps track of lexical errors

**Operations:**
- scan(): main method that scans the program and classifies the tokens, deciding if the program is lexically correct or not.
- output(): creates PIF.out and ST.out
- tokenize(line): splits a line into tokens (considering operators and strings)
- search_for_operators(line): searches for simple or compound operators in aline
and surrounds them with whitespace so they can be split later from the rest
- search_for_strings(line): searches for constant strings (text surrounded by “”),
adds them into a list and replaces them in the line with their index from that list
- some Boolean functions that check if a given token is an operator/separator/keyword/identifier/constant.

##### Regex:
identifier: ^[a-z][\w]*$
- begins with lowercase letter and has any number of letter/digit/underscore after
constant number: ^-?[1-9][0-9]*$
- optional ‘-‘ sign, must start with nonzero digit than has any number of digits
constant string: ^\"[A-Za-z0-9\.\?\!\-, ]*\"$
- must start and end with ", has any number of letters/digits U { . , ? ! space}
