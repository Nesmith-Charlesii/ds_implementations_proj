from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.list = []

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.list.append(self.head.data)
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node
        self.list.append(temporary_node.next.data)

    def prepend_node(self, data):
        node = Node(data)  # takes new data. assigns to variable 'node'
        temporary_node = self.head  # holds head of list as 'temporary_node'

        while temporary_node.prior is not None:
            temporary_node = temporary_node.prior

        temporary_node.prior = node  # assigns new node data as self.head
        return


