
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

def findClosestValueInBst(tree, target):
    return helper(tree, target, float("inf"))


def helper(tree, target, closest):
    if tree == None:
        return closest
    if abs(tree.value-target) < abs(closest-target): # 10-30 (=20) < 1000000-30(=9999970) 
        closest = tree.value # closest = 10
    
    left = tree.left # 10.left = 
    right = tree.right  #10.right = 
    if target < tree.value:
        return helper(left, target, closest)
    elif target > tree.value:
        return helper(right, target, closest)
    return closest



main_tree = BST(10)
tree1 = BST(5)
tree2 = BST(15)
tree11 = BST(2)
tree12 = BST(7)
tree111 = BST(1)
tree21 = BST(13)
tree212 = BST(14)
tree22 = BST(22)

main_tree.left = tree1
main_tree.right = tree2
tree1.left = tree11
tree1.right = tree12
tree11.left = tree111
tree2.left = tree21
tree2.right = tree22
tree21.right = tree212


# Play with the function:
print(findClosestValueInBst(main_tree, 12)) # change the target as you wish


#                   (10)
#               /           \
#       (5)                     (15)
#     /    \                 /        \
#   (2)     (7)          (13)          (22)
#  /                         \
#(1)                         (14)