z = [1, "hello", 3.14, True]
# lists can contain mixed data types

x = [9, 12, 7, 4, 11]

# Add element to a list
x.append(8)

# Sort list ascending , x.sort() defaults in ascending order
x.sort(reverse=True) # used reverse=True to print in descending order

print(x)  

# Algorithm to find the minimum value in an array
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)