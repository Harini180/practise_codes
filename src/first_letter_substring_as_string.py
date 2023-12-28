from functools import reduce
a = "George Raymond Richard Martin"
split_value = a.split()
new_value = list(map(lambda x:x[0], split_value))
final_value = reduce(lambda x,y:x+y , new_value)
# print(final_value)