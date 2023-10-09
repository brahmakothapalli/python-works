if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # my_list = [6, 0, 9, 11, 9]
    my_list = list(arr)
    maxi = my_list[0]
    for x in my_list:
        if x > maxi:
            maxi = x
    print(f"maximum num {maxi}")
    runner = my_list[0]
    for y in my_list:
        if (y < maxi) and (y > runner):
            runner = y
    print(f"runner num {runner}")
