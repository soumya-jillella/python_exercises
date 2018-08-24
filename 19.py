starting_point = input("starting point:")
ending_point = input("ending point:")
bus_fare=int(input("enter bus fare:"))
age=int(input("enter age:"))
if((age >= 5 and age <= 13) or age >= 60):
    print("there is no ticket for children below 5 years of age")
elif(age >= 5 or age <=13 or age>=60):
    print("there is 50% concession for this age group")
else:
    print("full ticket:")