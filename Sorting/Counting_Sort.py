# Counting Sort function
def countingSort(arr):
    max_val = max(arr)             # find the maximum value in the array
    count = [0] * (max_val + 1)    # create count array of size max_val+1, initialized to 0

    # Count the occurrences of each number
    while len(arr) > 0:
        num = arr.pop(0)           # remove the first element from arr
        count[num] += 1            # increment count for that number

    # Reconstruct the sorted array using the count array
    for i in range(len(count)):    # go through each number in count array
        while count[i] > 0:        # if number i occurred
            arr.append(i)          # add it back to the array
            count[i] -= 1          # decrease its count

    return arr                      # return the sorted array


mylist = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)  # call counting sort
print(mysortedlist)                   # print the sorted array

""" HOW IT WORKS ?
1. The countingSort function first determines the maximum value in the input array to establish the size of the count array.
2. It then counts the occurrences of each element in the input array and stores these counts in the count array.
3. Finally, it reconstructs the sorted array by appending each number the number of times it occurred.
4. The time complexity of Counting Sort is O(n + k), where n is the number of elements in the input array and k is the range of the input (i.e., the maximum value).
5. The space complexity is O(k) due to the count array.
6. Counting Sort is not a comparison-based sort and is stable, meaning it preserves the relative order of equal elements.
"""