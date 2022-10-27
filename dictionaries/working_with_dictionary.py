my_dict = {"name":"qababu", "profession":"QA Lead", "car":"Venue", "pin":99009}

print("\n***********print all keys in python****************** \n")
keys_list = list(my_dict.keys())
print("list of keys :: ", keys_list)
for key in keys_list:
    print(key, end=" ")
print("\n")

print("***********print all keys in python****************** \n")
values_list = list(my_dict.values())
print("list of vales :: ", values_list)
for val in values_list:
    print(val, end=" ")
print("\n")

print("*********** reading a value with key ****************** \n")
print("Key - profession :: Value - ", my_dict.get("profession"))

for dict in my_dict:
    print(dict)