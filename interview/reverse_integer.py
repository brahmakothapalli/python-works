
def reverse_integer(n):
    reversed_num = 0 # assigning zero to a variable
    while(n>0):
        remainder = n%10 # the remainder will be stored
        reversed_num = reversed_num * 10 + remainder
        n = n//10 # last digit will be removed
    return reversed_num

if __name__ == "__main__":
    num = int(input("Enter your +ve number: ")) # reading input from user
    reversed_number = reverse_integer(num)
    print(reversed_number) # prints the reversed number