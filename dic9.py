kvps = { '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5}
newdata = {'1' : 10, '3' : 30}
kvps.update(newdata)
x = sum(kvps.values())
print(x)