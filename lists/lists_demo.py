list1 = [1, 2, 3, 4, 5]
list2 = list1.copy()
print(list2)


tup1 = (1, 2, 3)
print(tup1[1])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [n%2==0 for n in lst]
lst3 = [n for n in lst if n%2 ==0]
print(lst2)
print(lst3)

my_list = [1, 2, 2, 3, 5, 3, 1, 5, 7]

print(my_list.pop(0))

print(my_list)
my_list.append(10)
print(my_list)
my_list.insert(6, 20)
print(my_list)