# Differentiate between the append() and extend() methods of a list.
# ANSWER
# The methods append() and extend() work on lists. While append() adds an element to the end of the list,
#  extend adds another list to the end of a list.

list,list2 = [1,2,3,5],[4,5,6,9,8]

# This is how append() works:
list.append(4) # it add 4 at the end of the list 
print(list)

# This is how extend() works:
list2.extend(list) # it extend list2 with list 
print(list2)