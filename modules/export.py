def exportsMissionPlannerFile(list_of_waypoints, fileName="waypoints.txt"):
    path ="./library/mission_planner"
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



def insertKmlHead(string):

    string+="""<Document>
            <name>AirRobot Recorded Flight Track</name>

            <Style id="yellowLine">
            <LineStyle>
            <color>5014F0FA</color>
            <width>2</width>
            </LineStyle>
            </Style>
            <Style id="redLine">
            <LineStyle>
            <color>ff3333CC</color>
            <width>3</width>
            </LineStyle>
            </Style>
            <Style id="greenLine">
            <LineStyle>
            <color>5014B482</color>
            <width>3</width>
            </LineStyle>
            </Style>
            <Style id="blueLine">
            <LineStyle>
            <color>90ff0000</color>
            <width>3</width>
            </LineStyle>
            </Style>
            <Style id="orangeLine">
            <LineStyle>
            <color>501478FF</color>
            <width>2</width>
            </LineStyle>
            </Style>
            <Style id="whiteLine">
            <LineStyle>
            <color>50FFFFFF</color>
            <width>2</width>
            </LineStyle>
            </Style>"""
    return string

def insertKmlFoot(string):
    string+="""\n</Document>"""
    return string


def insertKmlBoundary(list_of_points, string):
    string+="""
        <Placemark>
        <name>Flight Track</name>
        <description></description>
        <styleUrl>#redLine</styleUrl>
        <LineString>
        <altitudeMode>absolute</altitudeMode>
        <coordinates>
        """

    for point in list_of_points:
        string+="%.14f,%.14f,95" %(point.x, point.y)

    string+="""
        </coordinates>
        </LineString>
        </Placemark>"""

    return string


def insertKmlPath(list_of_points, string):
    string+="""
        <Placemark>
        <styleUrl>#yellowLine</styleUrl>
        <LineString>
        <width>20</width>
        <altitudeMode>absolute</altitudeMode>
        <coordinates>\n"""

    for point in list_of_points:
        string+="\t\t\t\t\t%.14f,%.14f,95\n" %(point.x, point.y)

    string+="""
        </coordinates>
        </LineString>
        </Placemark>"""

    return string




def exportsKML(list_of_waypoints, fileName="waypoints.kml"):
    path ="./library/kml/"
    text =""
    text = insertKmlHead(text)
    text = insertKmlPath(list_of_waypoints, text)
    text = insertKmlFoot(text)

    txtFile = open(path+fileName, "w+")
    txtFile.write(text)
    txtFile.close()
