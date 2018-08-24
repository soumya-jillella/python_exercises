list1 = ['A','B','C']
list2 = [1,2,3]
list1_list2 = [ (x,y) for x in list1 for y in list2]
print(list1_list2)