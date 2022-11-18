def reverse_method_01(actual_string):
    temp = "" # a variable with empty string
    n = len(actual_string)-1 # length of the string, starting with zero
    if n==0: # if string length is 1 return the same string
        temp = actual_string
    else:
        while(n>=0): # reading the each character of the string from the end and adding it to empty string
            temp=temp+actual_string[n]
            n-=1
    return temp


if __name__ == "__main__":
    given_string = input('Enter string to be reversed: ') # reading user input
    result_01 = reverse_method_01(given_string)
    print(result_01)