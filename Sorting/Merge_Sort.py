# Merge Sort function
def mergeSort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2
    leftHalf = arr[:mid]      # left half of array
    rightHalf = arr[mid:]     # right half of array

    # Recursively sort the left and right halves
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    # Merge the sorted halves and return
    return merge(sortedLeft, sortedRight)


# Merge function: merge two sorted arrays into one
def merge(left, right):
    result = []    # final merged array
    i = j = 0      # pointers for left and right arrays

    # Compare elements from left and right, append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])

    return result  # return merged sorted array


# --- Main code ---
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)       # call merge sort
print("Sorted array:", mysortedlist)   # print the sorted array

""" HOW IT WORKS ?
1. The mergeSort function recursively divides the array into halves until it reaches arrays of size 1 or 0, which are inherently sorted.
2. The merge function takes two sorted arrays and merges them into a single sorted array by comparing elements from each array.
3. The process continues until the entire array is merged and sorted.
4. The time complexity of Merge Sort is O(n log n) due to the divide-and-conquer approach.
5. The space complexity is O(n) because of the temporary arrays used for merging.
6. Merge Sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements."""