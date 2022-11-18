
numbers = [3, 5, 7, 9, 11] # a list

def square(x):
    # a method returns square of a given number
    return x * x

if __name__ == "__main__":
    result = map(square, numbers)
    squared_list = list(result)    
    print(f"The return type of map is {squared_list}")    





