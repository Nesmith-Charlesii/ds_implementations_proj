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
        node = Node(data)  # takes data argument. assigns data to variable 'node'
        temporary_node = self.head  # temporary_node holds self.head of list as 'temporary_node' (as to not overwrite the self.head)

        while temporary_node.prior is not None:
            temporary_node = temporary_node.prior

        temporary_node.prior = node  # assigns new node data as self.head
        self.list.insert(0, temporary_node.prior.data)  # inserts new node at the beginning of the list
        return

    def contains_node(self, data):
        if data in self.list:
            print(f"\nThe value of {data} is at index {self.list.index(data)} of this object\n")
