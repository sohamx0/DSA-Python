# Initial unsorted list
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# Length of the list
n = len(mylist)

# Outer loop: pick each element (starting from index 1) and insert it in the sorted part
for i in range(1, n):
    insert_index = i                   # Default position is the same spot
    current_value = mylist.pop(i)      # Remove the element at position i (to insert it later)

    # Inner loop: move backwards through the sorted part (0 → i-1)
    for j in range(i-1, -1, -1):
        # If a bigger element is found, update the position where current_value should go
        if mylist[j] > current_value:
            insert_index = j

    # Insert current_value into its correct position
    mylist.insert(insert_index, current_value)

# Final sorted list
print(mylist)


""" HOW IT WORKS ?
1. The outer loop iterates through each element starting from the second one (index 1).
2. The inner loop compares the current element with the elements in the sorted part (to the left) and finds the correct position for it.
3. The current element is then inserted into its correct position, shifting other elements as necessary.
4. This process is repeated until the entire list is sorted.
"""