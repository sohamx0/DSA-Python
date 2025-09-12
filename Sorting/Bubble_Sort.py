# What is sorting ?
# Sorting is the process of arranging data in a particular format or order.
# It can be in ascending or descending order.

# Initial unsorted list
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# Length of the list
n = len(mylist)

# Outer loop: controls the number of passes (n-1 passes needed)
for i in range(n-1):

    # Inner loop: compares elements up to the unsorted portion
    for j in range(n-i-1):

        # If the current element is greater than the next one, swap them
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# Final sorted list
print(mylist)



""" HOW IT WORKS ?
1. The outer loop runs n-1 times, where n is the length of the list.
2. The inner loop compares adjacent elements and swaps them if they are in the wrong order.
3. After each pass of the outer loop, the largest unsorted element "bubbles up" to its correct position at the end of the list.
4. This process is repeated until the entire list is sorted.
"""