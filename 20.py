salary = int(input("Please enter the salary:\n"))
rent = int(input("Please enter the house rent paid:\n"))
donations = int(input("Please enter the donations amount: \n"))
tax = 0
taxable_income = 0

if salary < 250000:
	print("Your income is not taxable. Enjoy!")
else:
	# I am just calculating taxable income and not exactly the tax
	taxable_income = salary - 250000

if rent > 0 and rent <=100000:
	taxable_income = taxable_income - rent
elif rent > 100000:
	taxable_income = taxable_income - 100000

if donations > 0 and donations <=80000:
	taxable_income = taxable_income - donations
elif donations > 80000:
	taxable_income = taxable_income - 80000

if taxable_income > 0:
	tax = taxable_income*(10/100)
else:
	print("You need not pay any tax. Do festival!")

print("=====================\n")
print("== Your Tax Details == \n")
print(f"Your salary: {salary} \n")
print(f"Congrats! Your tax: {tax}\n")
print("=====================")