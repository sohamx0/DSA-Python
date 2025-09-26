# Define a class for a tree node
class TreeNode:
  def __init__(self, data):        # Constructor initializes the node with data
    self.data = data               # Store the value (data) of the node
    self.left = None               # Pointer to the left child (initially None)
    self.right = None              # Pointer to the right child (initially None)

# Create tree nodes with given labels
root = TreeNode('R')   # Root node with data 'R'
nodeA = TreeNode('A')  # Node with data 'A'
nodeB = TreeNode('B')  # Node with data 'B'
nodeC = TreeNode('C')  # Node with data 'C'
nodeD = TreeNode('D')  # Node with data 'D'
nodeE = TreeNode('E')  # Node with data 'E'
nodeF = TreeNode('F')  # Node with data 'F'
nodeG = TreeNode('G')  # Node with data 'G'

# Connect children to form the tree structure
root.left = nodeA      # 'A' becomes left child of 'R'
root.right = nodeB     # 'B' becomes right child of 'R'

nodeA.left = nodeC     # 'C' becomes left child of 'A'
nodeA.right = nodeD    # 'D' becomes right child of 'A'

nodeB.left = nodeE     # 'E' becomes left child of 'B'
nodeB.right = nodeF    # 'F' becomes right child of 'B'

nodeF.left = nodeG     # 'G' becomes left child of 'F'

# Test: print the data of the left child of 'B' (which is 'E')

print("root.right.left.data:", root.right.left.data) #root which is R -> right which is B -> left which is E