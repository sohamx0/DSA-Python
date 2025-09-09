# Singly Linked Lists

# Node class to represent each element of the linked list
class Node:
    def __init__(self, data):
        self.data = data   # store the value
        self.next = None   # pointer to the next node (default None)

# Function to traverse and print all elements in the linked list
def traverse(head):
    current = head
    while current:  # loop until the end of the list
        print(current.data, end=" -> ")
        current = current.next
    print("null")  # mark end of list

# Append a new node at the end of the linked list
def append(head, data):
    new_node = Node(data)   # create new node
    if not head:            # if list is empty, new node becomes head
        return new_node
    current = head
    while current.next:     # move to the last node
        current = current.next
    current.next = new_node # attach new node at end
    return head

# Prepend a new node at the beginning of the list
def prepend(head, data):
    new_node = Node(data)   # create new node
    new_node.next = head    # point it to current head
    return new_node         # new node becomes head

# Insert a node at a given position
def insert(head, position, data):
    if position == 0:   # if inserting at beginning
        return prepend(head, data)
    new_node = Node(data)
    current = head
    for _ in range(position-1):   # move to node before insertion point
        if current is None:       # if position is invalid
            print("Position out of bounds")
            return head
        current = current.next
    # Insert new node between current and next
    new_node.next = current.next
    current.next = new_node
    return head

# Delete the first node with given key value
def delete(head, key):
    current = head
    prev = None
    # If head itself contains the key
    if current and current.data == key:
        return current.next  # move head to next node
    # Traverse until key is found
    while current and current.data != key:
        prev = current
        current = current.next
    if current is None:   # key not found
        print(f"{key} not found")
        return head
    # Skip the node to be deleted
    prev.next = current.next
    return head

# Search for a key in the linked list
def search(head, key):
    current = head
    pos = 0
    while current:
        if current.data == key:   # key found
            return pos
        current = current.next
        pos += 1
    return -1   # key not found

# ---------- Usage Example ----------
head = None

# Append nodes
head = append(head, 7)
head = append(head, 11)
head = append(head, 3)
traverse(head)  # 7 -> 11 -> 3 -> null

# Prepend a node
head = prepend(head, 99)
traverse(head)  # 99 -> 7 -> 11 -> 3 -> null

# Insert a node at position 2
head = insert(head, 2, 55)
traverse(head)  # 99 -> 7 -> 55 -> 11 -> 3 -> null

# Delete a node with value 11
head = delete(head, 11)
traverse(head)  # 99 -> 7 -> 55 -> 3 -> null

# Search for a node with value 55
pos = search(head, 55)
print("55 found at position:", pos)

# 