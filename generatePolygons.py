from modules.geometry import *
import randomPolygon

Polygon1 = Polygon( [Point(0.01,0.00), Point(1.00,0.02), Point(3.001,3.003), Point(2.01,5.03), Point(0,5), Point(0,2.33)] )

#### paramters
target_component = 0
seq = 0
frame = 3
command = 16
current = 0
autocontinue = 1
param1 = 0.0
param2 = 0.0
param3 = 0.0
param4 = 0.0
height = 200
#### paramters

txtFile = open("./library/waypoints.txt", "w+")
waypoint_line = ''
waypoint_line += 'QGC\tWPL\t110\n'
txtFile.write(waypoint_line)

for index, point in enumerate(Polygon1.vertices):
    temp_line ='%d\t%d\t%d\t%d\t'%(index, seq, frame, command)
    temp_line+='%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t1\n' %(current, autocontinue, param1, param2, point.x, point.y, height)
    txtFile.write(temp_line)
    #print(temp_line)
txtFile.close()


# index    seq    frame    command    current    autocontinue    param1    param2    point_x    point_y    point_z
#   0	    0	    0	     16	      0.000000	   0.000000	    0.000000  0.000000	-35.363209	149.165039	584.700012
