class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        '''  reverse a singly linked list '''
        # based on test file, initial node is head, prev is None
        # deal with empty lists
        if self.head is None:
            return

        # if the next node is none, we're at the end
        # make that the head node
        # and next_node point to previous to reverse
        if node.next_node is None:
            node.next_node = prev
            self.head = node
            return
        # move down the line until we get to the end
        self.reverse_list(node.next_node, node)
        # go back up chain and point current node to previous
        node.next_node = prev
