from Point import Point

class Rectangle:
	point1=None
	point2=None
	
	def __init__(self,p1,p2):
		self.point1=p1
		self.point2=p2
		
	def __str__(self):
		return "["+str(self.point1)+" - "+str(self.point2)+"]"