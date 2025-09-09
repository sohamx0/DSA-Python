def linearSearch(arr, targetVal):
    # loop through each index in the array
    for i in range(len(arr)):
        # check if the element at index i matches the target
        if arr[i] == targetVal:
            return i  # return index if found
    # if loop finishes without finding, return -1
    return -1


# unsorted list to search in
mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4  # target value to search

# call linear search
result = linearSearch(mylist, x)

# print result
if result != -1:
    print("Found at index", result)
else:
    print("Not found")



# use if not sorted List