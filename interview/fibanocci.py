# print fibanocci series upto nth term

x, y = 0, 1
n = int(input("Enter nth number: "))

if n < 0:
    print("Given number is negative, please enter the positive number")
elif n == 1:
    print(n)
else:
    for i in range(0, n):
        print(x, end =" ")
        p = x+y
        x = y
        y = p