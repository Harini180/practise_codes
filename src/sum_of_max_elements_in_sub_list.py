list=[[2,3,4,6],[23,4,5,6,7],[2,3,4,6]]
list2=[]
for i in list:
    maxe=i[0]
    for j in range(0,len(i)):
        if(i[j]>maxe):
            maxe=i[j]
    list2.append(maxe)
# print((list2))
sum=0
for i in list2:
    sum=sum+i
# print(sum)