# Partition function: chooses a pivot and arranges smaller and bigger elements around it
def partition(arr, low, high):
    pivot = arr[high]   # choose last element as pivot
    i = low - 1         # index of smaller element

    for j in range(low, high):
        # If current element is <= pivot, put it in the "smaller" region
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # Place pivot in its correct position (after smaller elements)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1  # return pivot index


# Quick sort function (recursive)
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array -> pivot gets its correct position
        pi = partition(arr, low, high)

        # Recursively sort elements before and after pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

quick_sort(arr, 0, n - 1)  # sort the array

print("Sorted Array:", arr)

""" HOW IT WORKS ?
1. The quick_sort function is called with the entire array. It checks if the current segment has more than one element.
2. The partition function selects a pivot (last element) and rearranges the array so that all elements smaller than the pivot are on the left, and all elements greater are on the right.
3. This process continues recursively until the entire array is sorted.
4. The time complexity of Quick Sort is O(n log n) on average, but it can degrade to O(n^2) in the worst case (e.g., when the array is already sorted).
5. The space complexity is O(log n) due to the recursive call stack.
6. Quick Sort is not a stable sorting algorithm, meaning that it may change the relative order of equal elements.
"""