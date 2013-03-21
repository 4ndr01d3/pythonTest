class Car:
    brand=None
    model=None
    year=None
    color="red"
	
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
        
    def toString(self):
        return "BRAND: "+self.brand+"\nMODEL: "+self.model+"\nYEAR: "+str(self.year)


class Bakkie(Car):
	capacity=None
	
	def __init__(self, brand, model, year,capacity):
		self.brand = brand
		self.model = model
		self.year  = year
		self.capacity  = capacity

	def toString(self):
		return "\nCAPACITY: "+str(self.capacity)+"Kgm"