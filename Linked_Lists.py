# Singly Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")

def append(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def prepend(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert(head, position, data):
    if position == 0:
        return prepend(head, data)
    new_node = Node(data)
    current = head
    for _ in range(position-1):
        if current is None:
            print("Position out of bounds")
            return head
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

def delete(head, key):
    current = head
    prev = None
    if current and current.data == key:
        return current.next  # deleting head
    while current and current.data != key:
        prev = current
        current = current.next
    if current is None:
        print(f"{key} not found")
        return head
    prev.next = current.next
    return head

def search(head, key):
    current = head
    pos = 0
    while current:
        if current.data == key:
            return pos
        current = current.next
        pos += 1
    return -1

head = None

head = append(head, 7)
head = append(head, 11)
head = append(head, 3)
traverse(head)  # 7 -> 11 -> 3 -> null

head = prepend(head, 99)
traverse(head)  # 99 -> 7 -> 11 -> 3 -> null

head = insert(head, 2, 55)
traverse(head)  # 99 -> 7 -> 55 -> 11 -> 3 -> null

head = delete(head, 11)
traverse(head)  # 99 -> 7 -> 55 -> 3 -> null

pos = search(head, 55)
print("55 found at position:", pos)
