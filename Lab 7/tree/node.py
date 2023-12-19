class Node:
    def __init__(self, info):
        self.__info = info
        self.__first_child = None
        self.__right_sibling = None
        self.__left_sibling = None

    @property
    def info(self):
        return self.__info

    @property
    def first_child(self):
        return self.__first_child

    @first_child.setter
    def first_child(self, node):
        self.__first_child = node

    @property
    def right_sibling(self):
        return self.__right_sibling

    @right_sibling.setter
    def right_sibling(self, node):
        self.__right_sibling = node

    @property
    def left_sibling(self):
        return self.__left_sibling

    @left_sibling.setter
    def left_sibling(self, node):
        self.__left_sibling = node