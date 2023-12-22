**Github Repository:** https://github.com/saltylex/milanguage/tree/main/Lab%202

### Milanguage

<<<<<<< HEAD
=======
**Github Repository: https://github.com/saltylex/milanguage**

>>>>>>> d3e6a7aba598a33062026d3b2af3298c8322f092
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
