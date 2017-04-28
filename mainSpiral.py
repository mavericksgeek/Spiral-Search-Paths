from __future__ import print_function
from modules.geometry import *
from modules.export import *

p1 = Point(-96.35111282486872,30.577821352883593)
p2 = Point(-96.35105252319403,30.577738952738226)
p3 = Point(-96.35098278437623,30.57762028386826)
p4 = Point(-96.35096243867648,30.577601831274514)
p5 = Point(-96.35103855263765,30.57748613262665)
p6 = Point(-96.35116430471045,30.577461636024072)
p7 = Point(-96.35140293901858,30.577502571702556)

Polygon1 = Polygon( [p1,p2,p3,p4,p5,p6,p7] )

p01 = Point(0.0,0.0)
p02 = Point(3.0,0.0)
p03 = Point(3.0,3.0)
p04 = Point(0.0,3.0)

Poly2 = Polygon( [p01,p02,p03,p04] )
print(Poly2.getArea())



#createWaypointFile(Polygon1.vertices, 'test.txt')

#poly = getRandomPolygon(20,-20,20,-20,5)
#print(poly)
