class Tree:
    def __init__(self, first_node):
        self.__head = first_node

    @property
    def head(self):
        return self.__head
