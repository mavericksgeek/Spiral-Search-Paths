from __future__ import print_function
from modules.geometry import *


#decomposedPolygons = [polygon1, polygon2, polygon3, polygon4]
polygon1.getSpiralPathToCentroid(3)
new_start_point = polygon1.getTransitionPathToNextPolygon(polygon2)
index = next( (i for i, point in enumerate(polygon2) if point == new_start_point)) # find the index of new_start_point in polygon2
polygon2 = getReorder()
polygon2.getSpiralPathToCentroid
