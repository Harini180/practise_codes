
str1 = 'My Name is Jessa'
list1 = []
str2 = str1.split(' ',7)

# print(str2)

for i in range(0,len(str2)):
    list1.append(str2[i][::-1])

# print(list1)

str3 = ' '.join(list1)

# print(str3)

