class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def num_unival_trees(root):
    count = 0
    if (root.data == root.left == root.right) or (root.data == None):
        count += 1
    return count
    
    
node1 = Node(0)
node2 = Node(1)
node3 = Node(0)
node4 = Node(1)
node5 = Node(0)
node6 = Node(1)
node7 = Node(1)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
node4.left = node6
node4.right = node7

print("The sum of unival trees is: ")
print(num_unival_trees(node1))