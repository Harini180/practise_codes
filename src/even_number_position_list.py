from functools import reduce
input = [ [11, 22, 33], [20, 40, 10]]
new_list = set(list(reduce(lambda x,y:x+y,input)))
list_new = list(new_list)
# print(list_new)
pos_1 =[]
for i in range(0,len(list_new)):
    if i%2 == 0:
        pos_1.append(list_new[i])
# print(pos_1)