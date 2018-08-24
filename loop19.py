a=int(input("enter a number"))
b=int(input("enter b number"))
if a<b:
    for a in range(a,b+1):
        print(a,end=" ")
else:
    for b in range(b,a+1):
        print(a,end=" ")
        a-=1