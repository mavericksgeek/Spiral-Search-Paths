from modules.geometry import *


p1 = Point(3,4) #create point by given x, y
print(p1)
p2 = Point(1,1)
print(p2)

print( p1.distanceToPoint(p2) ) #calculate the distance from p1 to p2

v1 = p2 - p1 #create vector by given end-point minus start-point
print(v1)

v2 = Vector(3,5) #create vector by given vector(Vx, Vy)
print(v2)

print( v1.dot(v2) )    #dot product
print( v1.cross(v2) )  #cross product

s1 = Segment(Point(0,0), Point(5,0)) #create segment by given two points
print(s1)

s2 = Segment(p1,p2)

print(s1.isIntersectSegment(s2)) #ask if two segments have intersection
print(p1.distanceToSegment(s1)) #disctance from a point to a segment
print(p1.isIntersectSegment(s1)) #ask if a point is lying on a segment


poly1 = Polygon([Point(0,0),Point(5,0),Point(3,5),Point(0,5)]) #create a polygon by given a list that includes points
print(poly1)

for point in poly1.vertices:
  #you can manipulate the vertices in the list
  print(point)


#createWaypointFile(poly1.vertices, 'test.txt')
