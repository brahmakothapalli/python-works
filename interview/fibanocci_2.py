n1, n2 = 0, 1
n = int(input("Enter the your range for fibanocci series:"))
if n < 0:
    print("Sorry, negative number is provided")
elif n==1:
    print(1)
else:
    for i in range(1, n):
        print(n1, end=" ")
        p = n1 + n2
        n1 = n2
        n2 = p
        