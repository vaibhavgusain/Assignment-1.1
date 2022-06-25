# Can you remove the whitespaces from the string “aaa bbb ccc ddd eee”?
#ANSWER

# method 1 
s='aaa bbb ccc ddd eee' #  remove whitespaces
new = "".join(s.split())
print(new)

# method 2 
s='aaa bbb ccc ddd eee'
new_one = s.replace(" ", "")
print(new_one)