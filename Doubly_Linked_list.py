
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def increase_length(self):
        self.length += 1

    def decrease_length(self):
        self.length -= 1

    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.increase_length()
            return
        else:
            self.insert_before(self.head, node)
            self.head = node

    def set_tail(self, node):
        if self.tail == None:
            self.set_head(node)
            self.increase_length()
            return
        else:
            self.insert_after(self.tail, node)
            self.tail = node

    # IRENE & JAREK'S
    def insert_before(self, node, node_to_insert):
        node_to_insert.prev = node.prev
        node_to_insert.next = node
        if node.prev:
            node.prev.next = node_to_insert
        node.prev = node_to_insert
        self.increase_length()

    #    if node_to_insert == self.head and node_to_insert == self.tail:
    #        return
    #    self.remove(node_to_insert)
    #    node_to_insert.prev = node.prev
    #    node_to_insert.next = node
    #    if node.prev == None:
    #        self.head = node_to_insert
    #    else:
    #        node.prev.next = node_to_insert
    #    node.prev = node_to_insert

    # IRENE & JAREK'S
    def insert_after(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        node_to_insert.prev = node
        node_to_insert.next = node.next
        if node.next is not None:
            node.next.prev = node_to_insert
        node.next = node_to_insert
        self.increase_length()

    # def insert_after(self, node, node_to_insert):
    #    if node_to_insert == self.head and node_to_insert == self.tail:
    #        return
    #    self.remove(node_to_insert)
    #    node_to_insert.prev = node
    #    node_to_insert.next = node.next
    #    if node.next == None:
    #        self.tail = node_to_insert
    #    else:
    #        node.next.prev = node_to_insert
    #    node.next = node_to_insert

# IRENE & JAREK:

    def insert_at_position(self, position, node_to_insert):
        if position > self.length or position < 0:
            raise ValueError("Position not in range.")
        temp = None
        curr = self.head
        counter = 0
        if position == 0:
            self.set_head(node_to_insert)
            return
        if position == self.length:
            self.set_tail(node_to_insert)
            return
        while counter < position:
            temp = curr
            counter += 1
            curr = curr.next
        node_to_insert.prev = temp
        node_to_insert.next = temp.next
        temp.next = node_to_insert
        if node_to_insert.next:
            node_to_insert.next.prev = node_to_insert
        self.increase_length()

    # def insert_at_position(self, position, node_to_insert):
    #    if position == 1:
    #        self.set_head(node_to_insert)
    #        return
    #    node = self.head # In this def, we consider position 1 to be the first (head) node.
    #    currentPosition = 1
    #    while node is not None and currentPosition != position:
    #        node = node.next
    #        currentPosition += 1
    #    if node is not None:
    #        self.insert_before(node, node_to_insert)
    #    else:
    #        self.set_tail(node_to_insert)

    def remove_nodes_with_value(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.updateNodePointers(node)
        self.decrease_length()

    def search_node_with_value(self, value):
        node = self.head
        counter = 0
        while node is not None and node.value != value:
            node = node.next
            counter += 1
        return node is not None, counter

    def updateNodePointers(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def print_traverse(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return arr

    def print_reverse(self):
        arr = []
        curr = self.tail
        while curr:
            arr.append(curr.value)
            curr = curr.prev
        return arr

    def reverse(self):
        if self.head is None and self.head.next is None:
            return
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        self.head = temp.prev


node1 = Node(1)
node5 = Node(5)
node3 = Node(3)
node2 = Node(2)
node7 = Node(7)
my_linked_list = DoublyLinkedList()
my_linked_list.set_head(node1)
my_linked_list.set_tail(node3)
print("Traverse before insert:", my_linked_list.print_traverse())
my_linked_list.insert_before(node3, node5)  # [1, 5, 3]
my_linked_list.insert_after(node5, node2)  # [1, 5, 2, 3]
my_linked_list.insert_at_position(0, node7)
print("Traverse after insert:",
      my_linked_list.print_traverse())  # [1, 7, 5, 2, 3]
# print("Reverse:", my_linked_list.print_reverse())
my_linked_list.reverse()
print("New_traverse:", my_linked_list.print_traverse())
