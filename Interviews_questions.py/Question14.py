import re
# Write a regular expression that will accept an email id. Use the re module
e=re.search(r'[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$','abc@gmail.com')
print(e.group())