string = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M".split(
    " ")
print(string)


#
#
def caps(l):
    if l.isalpha():
        return l.capitalize()
    else:
        return ''


#
#
my_list = list(map(caps, string))

print(" ".join(my_list))


