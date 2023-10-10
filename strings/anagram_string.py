str1 = "silent"
str2 = "listen"
flag = True
if len(str1) == len(str2):
    for ch in str1:
        if ch not in str2:
            flag = False
    if flag == True:
        print("******* given strings are anagram ***************")
    else:
        print("******* given strings are not anagram ***********")
else:
    print("******* given strings are not anagram ***********")

