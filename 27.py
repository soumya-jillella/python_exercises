year = int(input("enter a year:"))

if year % 12 == 8:
	animal = "Dragon"
elif year % 12 == 9:
	animal = "Snake"
elif year % 12 == 10:
	animal = "Horse"
elif year % 12 == 11:
	animal = "Sheep"
elif year % 12 == 0:
	animal = "Monkey"
elif year % 12 == 1:
	animal = "Rooster"
elif year % 12 == 2:
	animal = "Dog"
elif year % 12 == 3:
	animal = "Pig"
elif year % 12 == 4:
	animal = "Rat"
elif year % 12 == 5:
	animal = "Ox"
elif year % 12 == 6:
	animal = "Tiger"
elif year % 12 == 7:
	animal = "Hare"

print(f"{year} is the year of {animal}")