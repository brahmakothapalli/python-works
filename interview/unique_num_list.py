
# finding unique number in the given list
my_list = [1, 2, 2, 3, 5, 3, 1, 5, 7]
l = len(my_list)
m = 0
if not my_list:
    print("Given list is empty")
else:
    while(m < l):
        num = my_list.pop(0)
        if num in my_list:
            my_list.remove(num)
        else:
            print("unique number is ",num)
            break
        m+=1