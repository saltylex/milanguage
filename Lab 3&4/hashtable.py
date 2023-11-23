from collections import deque


class HashTable:
    def __init__(self, size):
        self.size = size
        self.nr_elements = 0
        self.elements = [deque() for _ in range(size)]

    def hash(self, key):
        key = str(key)
        return self.val_compute(key) % self.size

    @staticmethod
    def val_compute(key):
        return sum(ord(character) for character in str(key))

    def add(self, key):
        value = self.hash(key)  # compute deque position in hashtable for key
        element_list = self.elements[value]  # retrieve deque

        # search if we already added it
        for index, element in enumerate(element_list):
            if element == key:
                return value, index  # if exists we don't add

        # else add
        element_list.append(key)
        self.nr_elements += 1
        return value, len(element_list) - 1

    def exists(self, key):
        value = self.hash(key)  # compute deque position in hashtable for key
        element_list = self.elements[value]  # retrieve deque
        return any(element == key for element in element_list)  # check

    def get_position(self, key):
        value = self.hash(key)  # compute deque position in hashtable for key
        element_list = self.elements[value]  # retrieve deque
        for index, element in enumerate(element_list):
            if element == key:
                return value, index  # return position
        return False

    def __str__(self):
        string = ""
        for i, element_list in enumerate(self.elements):
            if element_list:
                string_list = f"{i} -> "
                for el in element_list:
                    string_list += f"{el} | "
                string += string_list + "\n"

        if string == "":
            return "empty"
        return string

    def size(self):
        return self.nr_elements
