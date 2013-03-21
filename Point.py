import math

class Point:
	x=None
	y=None
	
	def __init__(self,coordinate_x,coordinate_y):
		self.x=coordinate_x
		self.y=coordinate_y
		
	def __str__(self):
		return "("+str(self.x)+", "+str(self.y)+")"

	def distance(self,p2):
		return math.sqrt((p2.x-self.x)**2 + (p2.y-self.y)**2)
