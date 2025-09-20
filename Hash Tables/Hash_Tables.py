# The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting data can be done really quickly, even for large amounts of data.

# make a simple list 

my_list = [None, None, None, None, None , None, None, None, None, None]

# create a simple hash function 

def hash_function(value):
  sum_of_chars = 0
  for char in value:             # loop through each character in the string
    sum_of_chars += ord(char)    # get ASCII code of the char and add to sum

  return sum_of_chars % 10       # take remainder when divided by 10

#adding a name 

def add(name):
  index = hash_function(name)
  my_list[index] = name

add('Bob')
print(my_list)
add('Pete')
add('Jones')
add('Lisa')
add('Amy')

# check if it contains a name

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))