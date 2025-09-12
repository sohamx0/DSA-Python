# Initial unsorted list
mylist = [64, 34, 25, 5, 22, 11, 90, 12]

# Length of the list
n = len(mylist)

# Outer loop: iterate over each index of the list (except the last one, since it’ll already be sorted)
for i in range(n-1):
    min_index = i  # Assume the current position has the minimum value

    # Inner loop: find the index of the smallest element in the remaining unsorted part
    for j in range(i+1, n):
        if mylist[j] < mylist[min_index]:
            min_index = j  # Update min_index if a smaller element is found

    # Remove the smallest element from its current position
    min_value = mylist.pop(min_index)

    # Insert the smallest element at the correct sorted position (index i)
    mylist.insert(i, min_value)

# Final sorted list
print(mylist)



""" HOW IT WORKS ?
1. The outer loop iterates through each index of the list, treating it as the current position to fill with the smallest unsorted element.
2. The inner loop finds the smallest element in the remaining unsorted part of the list.
3. The smallest element is then removed from its current position and inserted at the correct sorted position.
4. This process is repeated until the entire list is sorted.
"""