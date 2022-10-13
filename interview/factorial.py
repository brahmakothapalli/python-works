from math import factorial


n = int(input("Enter the number for factorial: "))
i = 1
facto = 1
if n < 0:
    print("Negative number is provided, please provide positive number")
else:
    while(i<=n):
        facto = facto * i
        i+=1
print(f"The factorial of the given number {n} is {facto}")
