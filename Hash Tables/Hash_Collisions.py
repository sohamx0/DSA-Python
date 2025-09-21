"""We need to handle collisions in our hash table.
if we have two different names that hash to the same index,
we need to be able to store both names."""

my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)
  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index].append(name)

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Amy')
print(my_list)

# Here Amy and Bob both hash to index 5, so they are both stored in a list at that index.