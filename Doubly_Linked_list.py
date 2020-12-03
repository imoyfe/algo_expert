
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
      
    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.insert_before(self.head, node)


    def set_tail(self, node):
        if self.tail == None:
            self.set_head(node)
            return
        else:
            self.insert_after(self.tail, node)
 

    def insert_before(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev 
        node_to_insert.next = node
        if node.prev == None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert


    def insert_after(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next 
        if node.next == None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert
        

    def insert_at_position(self, position, node_to_insert):
        if position == 1:
            self.set_head(node_to_insert)
            return
        node = self.head # In this def, we consider position 1 to be the first (head) node.
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insert_before(node, node_to_insert)
        else:
            self.set_tail(node_to_insert)


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


    def search_node_with_value(self, value):
        node = self.head
        counter = 0
        while node is not None and node.value != value:
            node = node.next
            counter +=1
        return node is not None , counter


    def updateNodePointers(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None



node1 = Node(1)
node5 = Node(5)
node3 = Node(3)
node2 = Node(2)
node7 = Node(7)
my_linked_list = DoublyLinkedList()
my_linked_list.set_head(node1)
my_linked_list.set_tail(node3)
my_linked_list.insert_before(node3, node5)
my_linked_list.insert_after(node5, node2)
print("From head to tail:", my_linked_list.head.value, "->", my_linked_list.head.next.value, "->", my_linked_list.head.next.next.value, "->", my_linked_list.head.next.next.next.value)
print("From tail to head:", my_linked_list.tail.value, "<-", my_linked_list.tail.prev.value, "<-", my_linked_list.tail.prev.prev.value, "<-", my_linked_list.tail.prev.prev.prev.value)

### Next steps: create reverse method.