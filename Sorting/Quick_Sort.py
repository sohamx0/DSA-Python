# Partition function: places pivot in correct position
# and ensures all smaller elements are on left, larger on right
def partition(array, low, high):
    pivot = array[high]       # choose last element as pivot
    i = low - 1               # index for smaller element

    # loop through the array segment
    for j in range(low, high):
        if array[j] <= pivot:  # if current element <= pivot
            i += 1              # move index for smaller element
            array[i], array[j] = array[j], array[i]  # swap current element with element at i

    # place pivot after last smaller element
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1   # return the pivot index


# Quick Sort function (recursive)
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1   # set high to last index if not provided

    if low < high:
        # Partition the array, pivot_index is now at correct position
        pivot_index = partition(array, low, high)

        # Recursively sort elements before pivot
        quicksort(array, low, pivot_index - 1)

        # Recursively sort elements after pivot
        quicksort(array, pivot_index + 1, high)


mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)   # call quicksort
print(mylist)       # print sorted array

""" HOW IT WORKS ?
1. The quicksort function is called with the entire array. It checks if the current segment has more than one element.
2. The partition function selects a pivot (last element) and rearranges the array so that all elements smaller than the pivot are on the left, and all elements greater are on the right.
3. This process continues recursively until the entire array is sorted.
4. The time complexity of Quick Sort is O(n log n) on average, but it can degrade to O(n^2) in the worst case (e.g., when the array is already sorted).
5. The space complexity is O(log n) due to the recursive call stack.
6. Quick Sort is not a stable sorting algorithm, meaning that it may change the relative order of equal elements.
"""