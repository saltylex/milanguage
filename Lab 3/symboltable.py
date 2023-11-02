from hashtable import HashTable


class SymbolTable:

    def __init__(self, size):
        self.__ht = HashTable(size)

    def add(self, key):
        return self.__ht.add(key)

    def get_position(self, key):
        return self.__ht.get_position(key)

    def exists(self, key):
        return self.__ht.get_position(key)

    def __str__(self):
        return str(self.__ht)

    def size(self):
        return self.__ht.size()


if __name__ == "__main__":
    c = SymbolTable(100)
    print(c.add('A'))
    print(c.add('Ad'))
    print(c.add('aa'))
    print(c.add('aa'))
    print(str(c))
