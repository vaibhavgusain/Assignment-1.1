#  How do you open a file for writing?

# ANSWER
# Let’s create a text file on our Desktop and call it tabs.txt.
# To open it to be able to write to it, use the following line of code-
file = open("nothing.txt",'w')

# This opens the file in writing mode. You should close it once you’re done.
print(file.close())