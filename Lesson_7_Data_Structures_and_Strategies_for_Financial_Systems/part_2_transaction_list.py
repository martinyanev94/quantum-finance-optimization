class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TransactionList:
    def __init__(self):
        self.head = None

    def add_transaction(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_transactions(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
