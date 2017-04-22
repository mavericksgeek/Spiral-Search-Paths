from __future__ import print_function
from modules.geometry import *

p1 = Point(0,0)
p2 = Point(6,6)

p3 = Point(0,6)
p4 = Point(6,0)

s1 = Segment(p1,p2)
s2 = Segment(p3,p4)

v1 = Vector(3,3)

# X = [Point(0,0), Point(0,6), Point(6,6), Point(6,0)]
# poly1 = Polygon(X)
# print(poly1.getSpiralPathToCentroid(5))


Y = [Point(30.577821352883593, -96.35111282486872),Point(30.577738952738226, -96.35105252319403), Point(30.57762028386826, -96.35098278437623),Point(30.577601831274514, -96.35096243867648),Point(30.57748613262665, -96.35103855263765),Point(30.577461636024072, -96.35116430471045),Point(30.577502571702556,-96.35140293901858)]
#Y = [Point(0,0), Point(0,8) Point(3,0)]
#print(Y[0])
poly2 = Polygon(Y)

print("centroid:", poly2.centroid)
result = poly2.getSpiralPathToCentroid(20)

for point in result:
    print(point)
