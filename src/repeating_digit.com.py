
input_list = [1, 2, 4, 5, 5, 5, 5, 6, 5, 5, 6, 7, 7, 8, 9]
pos = []
search_element = 5
for i in range(0,len(input_list)):
    if input_list[i]==search_element and input_list[i+1]!=input_list[i] :
        pos.append(i)
    if input_list[i]==search_element and input_list[i-1]!=input_list[i]:
         pos.append(i)
         #break  (first set of repeating values index to be returned (i.e) 3 and 6 only)
