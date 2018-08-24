def power(a,n):
	if (n == 0):
		return 1
	elif (int(n%2) == 0):
		return (power(a,int(n/2))) * (power(a,int(n/2)))
	else:
		return (a * power(a,int(n/2))) * (power(a,int(n/2)))
a = 3; n = 2		
print(power(a,n))