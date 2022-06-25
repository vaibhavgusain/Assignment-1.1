# What is frozen set in Python?

# First ,let's discuss what a set is . A set is collection of items, where there
# cannot be any duplicates. A set is also  unordered.

myset= {1,3,5,5,6}
print(myset) # it return 1,3,5,6

# This means that we cannot index  it
# print(myset[0])

# However, a set is mutable. A frozen set is immutable. This means we
# cannot change its values. This also makes it eligible to be used as a key for 
# a dictionary.

myset = frozenset([1,3,2,2])
print(myset)
print(type(myset)) #<class 'frozenset'>
