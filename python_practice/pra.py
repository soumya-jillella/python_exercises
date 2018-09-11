class Vehicle:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

v = Vehicle("Hero","Bajaj",2016)
print(v)

print(Vehicle.Hero)