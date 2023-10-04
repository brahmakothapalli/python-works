my_tuple = 'Python' * 3
print(my_tuple)

list_1 = [1, 2, 3]
print("list1 is ", list_1)
print(f"length of the list1 is {len(list_1)}")
list_2 = list_1
print("list2 is ", list_2)
list_1.append(list_2)
print(f"length of the list1 after appending is {len(list_1)}")
print("after appending list1 is ", list_1)
print("list1 index 3 value is ", list_1[3])

list_3 = [4, 5, 6]
list_4 = list_3
print(list_3 + list_4)
