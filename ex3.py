numbers ={
	"first" : 1,
	"second" : 2,
	"third" : 3}
squared_numbers = {key:value**2 for key,value in numbers.items()}
print(squared_numbers)


a={num: num**2 for num in [1,2,3,4,5]}
print(a)

numbers = (1,2,3,4)
numbers[0] = 3
