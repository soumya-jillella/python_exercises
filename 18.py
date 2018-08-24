a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if (a==b and a==c and b==c):
    print (3) 
elif (a==b and a!=c and b!=c) or (b==c and b!=a and c!=a) or (c==a and c!=b and a!=b):
    print (2) 
else:
    print (0) 

    