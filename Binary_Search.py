def binarySearch(arr, targetVal):
    # initialize the left and right pointers
    left = 0
    right = len(arr) - 1

    # keep looping until the search space is valid
    while left <= right:
        # find the middle index
        mid = (left + right) // 2

        # check if the middle element is the target
        if arr[mid] == targetVal:
            return mid  # found, return index

        # if target is bigger, search the right half
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            # if target is smaller, search the left half
            right = mid - 1

    # if not found in the array
    return -1


# sorted list to search in
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11  # target value to search

# call binary search
result = binarySearch(mylist, x)

# print result
if result != -1:
    print("Found at index", result)
else:
    print("Not found")


# use if sorted List