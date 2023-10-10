string = "level"
new_string = string[::-1]
print(new_string)
if string.__eq__(new_string):
    print("Palindrome")
else:
    print("Not Palindrome")