class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def sum_tree(root):
    if (root == None):
        return 0
    return root.data + sum_tree(root.left) + sum_tree(root.right)


#          5
#       /      \
#     8         9
#    /  \          \
#   6    4           7

node1 = Node(5)
node2 = Node(8)
node3 = Node(9)
node4 = Node(6)
node5 = Node(4)
node6 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6


print("The sum of the given tree is: ")
print(sum_tree(node2))
