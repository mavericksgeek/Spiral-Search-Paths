from __future__ import print_function
from modules.geometry import *

p1 = Point(0,0)
p2 = Point(6,6)

p3 = Point(0,6)
p4 = Point(6,0)

s1 = Segment(p1,p2)
s2 = Segment(p3,p4)

v1 = Vector(3,3)

X = [Point(0,0), Point(0,6), Point(6,7), Point(6,0)]
poly1 = Polygon(X)
poly1.getSpiralPathToCentroid(2) #self.endpoint is created
print("before", poly1)
poly1.reorderVertice(2)
print("after", poly1)

Y = [Point(0,0), Point(0,6), Point(-6,6), Point(-6,0)]
poly2 = Polygon(Y)

print(poly1.getTransitionPathToNextPolygon(poly2))

# print(poly1.getSpiralPathToCentroid(5))

"""
Y = [Point(30.577821352883593, -96.35111282486872),Point(30.577738952738226, -96.35105252319403), Point(30.57762028386826, -96.35098278437623),Point(30.577601831274514, -96.35096243867648),Point(30.57748613262665, -96.35103855263765),Point(30.577461636024072, -96.35116430471045),Point(30.577502571702556,-96.35140293901858)]
poly2 = Polygon(Y)
result = poly2.getSpiralPathToCentroid(20)
"""

def printSpiralPathWithKmlFormat(spiralpath):
    print("End Point:", spiralpath[-1])
    for point in result:
        print(point)

A = {p1, p2, p3}
B = {p2, p3}
#print(A.intersection(B))




#printSpiralPathWithKmlFormat(result)


"""
#decomposedPolygons = [polygon1, polygon2, polygon3, polygon4]
polygon1.getSpiralPathToCentroid(3)
new_start_point = polygon1.getTransitionPathToNextPolygon(polygon2)
index = next( (i for i, point in enumerate(polygon2) if point == new_start_point)) # find the index of new_start_point in polygon2
polygon2 = getReorder()
polygon2.getSpiralPathToCentroid
"""

