# Function to merge two halves
def merge(left_half, right_half):
    merged = []   # final merged sorted array
    i = j = 0     # pointers for left and right halves

    # Compare elements from both halves and pick the smaller one
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged.append(left_half[i])  # take from left
            i += 1
        else:
            merged.append(right_half[j]) # take from right
            j += 1

    # If anything is left in left_half, dump it into merged
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    # If anything is left in right_half, dump it into merged
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged


# Function to perform merge sort
def merge_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2

    # Recursively sort the left half
    left_half = merge_sort(arr[:mid])

    # Recursively sort the right half
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

sorted_arr = merge_sort(arr)  # call merge sort

print("Sorted Array:", sorted_arr)

""" HOW IT WORKS ?
1. The merge_sort function recursively divides the array into halves until it reaches arrays of size 1 or 0 (base case).
2. The merge function then merges two sorted halves into a single sorted array by comparing elements from both halves.
3. This process continues recursively until the entire array is sorted.
4. The time complexity of Merge Sort is O(n log n) in all cases (best, average, worst) due to the divide-and-conquer approach.
5. The space complexity is O(n) because it requires additional space for the temporary arrays used during merging.
6. Merge Sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements.
"""