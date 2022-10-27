def square(x):
    return x*x

if __name__ == "__main__":
    my_list = list(map(int, input("enter your list:").split()))
    print(type(my_list))
    print(my_list)
    squared_list = list(map(square, my_list))
    print(squared_list)
    a = 2/6
    print(format(a, '.6f'))
    
