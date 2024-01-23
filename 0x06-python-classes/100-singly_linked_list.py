#!/usr/bin/python3
# 101-square.py
"""Defines a singly linked list"""


class Node:
    """Defines a class Node"""
    def __init__(self, data, next_node=None):
        """Initializes an instance to the class Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to data in class Node
        Return:
            int: data to Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to data in class Node
        Args:
            value (int): value of data
        Raises:
            TypeError: if data is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter to next_node of class Node
        Return:
            int : data to next_node in class Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to next_node in class Node
        Args:
            value (int): value to next node
        Raises:
            TypeError: if not a Node Object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Singly linked list"""


class SinglyLinkedList:
    """Defines a class SinglyLinkedList"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new node"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        now = self.head
        while now.next_node is not None and now.next_node.data < value:
            now = now.next_node

        new_node.next_node = now.next_node
        now.next_node = new_node

    def __str__(self):
        outcome = ""
        now = self.head
        while now:
            outcome += str(now.data) + "\n"
            now = now.next_node
        return outcome.strip()
