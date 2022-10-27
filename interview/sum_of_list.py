from operator import indexOf, le


my_list = [6,7,8,9,10,11,12,13,14]
count = len(my_list)
n=0
sums = []
sum=0
for e in my_list:
    # if my_list.index(e) != n:
    # sum = sum+e
    sum=sum+e 
while n < count:
    sums.append(sum-my_list[n])
    n+=1
# print(sums)
print(f"{min(sums)}  {max(sums)}")
# print(max(sums))
# print(min(sums))

# same_list = [5,5,3,5,5]
# for v in same_list:
#     print(same_list.index(v))

