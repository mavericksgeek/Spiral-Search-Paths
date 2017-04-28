def createWaypointFile(list_of_waypoints, fileName="waypoints.txt"):
    path ="./library/"
    ######## paramters ########
    target_component = 0
    seq = 0
    frame = 3
    command = 16
    current = 0
    autocontinue = 0
    param1 = 0.0
    param2 = 0.0
    param3 = 0.0
    param4 = 0.0
    height = 200
    ######## paramters ########

    txtFile = open(path+fileName, "w+")
    waypoint_line = ''
    waypoint_line += 'QGC WPL 110\n'
    txtFile.write(waypoint_line)

    for index, point in enumerate(list_of_waypoints):
        if index == 0:
            temp_line ='%d\t%d\t%d\t%d\t'%(index, seq, 0, command)
        else:
            temp_line ='%d\t%d\t%d\t%d\t'%(index, seq, frame, command)
        #temp_line+='%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t1\n' %(current, autocontinue, param1, param2, point.x, point.y, height)
        temp_line+='%.6f\t%.6f\t%.6f\t%.6f\t%.14f\t%.14f\t%.14f\t1\n' %(current, autocontinue, param1, param2, point.y, point.x, height)
        txtFile.write(temp_line)
        #print(temp_line)
    txtFile.close()
