from modules.geometry import *
import randomPolygon

p1 = Point(-96.35111282486872,30.577821352883593)
p2 = Point(-96.35105252319403,30.577738952738226)
p3 = Point(-96.35098278437623,30.57762028386826)
p4 = Point(-96.35096243867648,30.577601831274514)
p5 = Point(-96.35103855263765,30.57748613262665)
p6 = Point(-96.35116430471045,30.577461636024072)
p7 = Point(-96.35140293901858,30.577502571702556)

Polygon1 = Polygon( [p1,p2,p3,p4,p5,p6,p7] )


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
    #temp_line+='%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t1\n' %(current, autocontinue, param1, param2, point.x, point.y, height)
    temp_line+='%.6f\t%.6f\t%.6f\t%.6f\t%.14f\t%.14f\t%.14f\t1\n' %(current, autocontinue, param1, param2, point.x, point.y, height)
    txtFile.write(temp_line)
    #print(temp_line)
txtFile.close()


# index    seq    frame    command    current    autocontinue    param1    param2    point_x    point_y    point_z
#   0	    0	    0	     16	      0.000000	   0.000000	    0.000000  0.000000	-35.363209	149.165039	584.700012
