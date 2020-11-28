
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array
    


a = Node("A")
a.addChild("B")
a.addChild("C")
a.addChild("D")
a.children[0].addChild("E")
a.children[0].addChild("F")
a.children[2].addChild("G")
a.children[2].addChild("H")
a.children[0].children[1].addChild("I")
a.children[0].children[1].addChild("J")
a.children[2].children[0].addChild("K")

print(a.depthFirstSearch([]))



# print(a.name)
# print(a.children[0].name)
# print(a.children[0].children[0].name)
# print(a.children[0].children[1].name)
