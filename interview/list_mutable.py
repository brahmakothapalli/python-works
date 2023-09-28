# list are mutable
list1 = [3, 4, 5, 6, 7, 8, 9]
print("given list --> ", list1)
print("value at index 3 --> ", list1[3])
list1[3] = 10
print("now value 6 is replaced by -->{} ".format(list1[3]), list1)
list1.append(20)
print("value 20 is is added to the list", list1)
list1.remove(4)
print("removed value 4 from the list ", list1)
