# Linked lists 

# Q) Implement a singly linked list with: Insert at beginning, end, and middle, Delete by value and by position, Search for an element

class Node:
    def __init__ (self, data):
        self.data = data 
        self.next = None

def List(head):
    current = head
    while current:
        print(current.data, end=" ->")
        current = current.next
    print("None")

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, position, data):
    if position == 0:
        return insert_at_beginning(head, data)
    new_node = Node(data)
    current = head
    for _ in range(position - 1):
        if current is None:
            print("Position out of bounds")
            return head
        current = current.next
        
    new_node.next = current.next
    current.next = new_node
    return head

def delete_by_value(head, key):
    current = head
    prev = None
    if current and current.data == key:
        return current.next
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
head = insert_at_end(head, 1)
head = insert_at_end(head, 2)
head = insert_at_end(head, 3)
List(head)
head = insert_at_beginning(head, 0)
List(head)
head = insert_at_position(head, 2, 1.5)
List(head)
head = delete_by_value(head, 2)
List(head)
print(search(head, 3))