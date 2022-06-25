# Can you explain the filter(), map(), and reduce() functions?
# Answer 

# 1. filter()- This function lets us keep the values that satisfy some conditional logic.
#  Let’s take an example.

print(list(filter(lambda x:x>4, range(7)))) #This filters in the elements from 0 to 6 that are greater than the number 4.

# 2. map()- This function applies a function to each element in the iterable
print(set(map(lambda x:x**3, range(7)))) #This calculates the cube for each element in the range 0 to 6 and stores them in a set

#3.reduce()- This function reduces a sequence pair-wise, repeatedly until we arrive at a single value

print(reduce(lambda x,y:y-x, [1,2,3,4,5]))