color_set1 = ["red","orange","green","blue","white"]
color_set2 = ["black","yellow","green","blue"]
color_set1 = [x for (i,x) in enumerate(color_set1) if i not in (2,3)]
print(color_set1)
color_set2 = [x for (i,x) in enumerate(color_set2) if i not in (2,3)]
print(color_set2)