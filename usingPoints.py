from Point import Point
from Rectangle import Rectangle


pointa=Point(10.0,5.0)
pointb=Point(1.0,9.0)

print "the distance of the point "+str(pointa)+" and ther point "+str(pointb)+" is:"+str(pointa.distance(pointb))


rectangle=Rectangle(pointa,pointb)

print rectangle