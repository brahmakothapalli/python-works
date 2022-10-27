# p = map(int, input().rstrip().split())
# print(list(p))

from xml.dom.minidom import TypeInfo


def read_integers():
    a = input("enter values: ").split()
    print(a)
    print(type(a[0]))

def read_integers_using_map():
    a = map(int, input("enter values: ").split())
    my_list = list(a)
    print(my_list)
    print(type(my_list[0]))

def read_float_values_using_map():
    a = map(float, input("enter float values with comma seperated: ").split(","))
    my_list = list(a)
    print(my_list)
    print(type(my_list[0]))

def read_integers_set():
    a = map(int, input("enter values: ").split())
    my_list = set(a)
    print(my_list)
    print(type(my_list[0]))

if __name__ == "__main__":
    print("reading intergers")
    read_integers()
    print("reading intergers using map")
    read_integers_using_map()
    print("rading float values")
    read_float_values_using_map()
    read_integers_set()