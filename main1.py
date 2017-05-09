            #############################################
             ### Application Programming Interface #####
              #########################################

########################################################################
### Use these common names so that we can merge code easily later.   ###
### DO NOT CHANGE THE FUNCTION NAMES, INPUTS, OR RETURN OUTPUT TYPE! ###
########################################################################
from __future__ import print_function
from modules.geometry import *
from modules.export import *
from subprocess import call

## Function ##############################################
# Reads input.txt and converts the points into a boundry polygon
def polygon_from_disk():
    # read from file
    f = open("input.txt", "r")
    lines = f.readlines()
    points = []
    polygon = Polygon([Point(0,0)]) #Empty Polygon
    xory = 0 # x = 0 , 1 = y , 2 = both
    x = -1
    y = -1
    for line in lines:
        line = "".join(line.split()) # remove ALL whitespace
        line = line.split(",")
        if line != "":
            x = float(line[0])
            y = float(line[1])
            p = Point(x,y)
            points.append(p)
            xory = 0
            x = -1
            y = -1
        else:
            print("Error from_disk(): Unknown character" + str(line))
    polygon.vertices = points
    return polygon

# (INTERNAL) Returns a polygon; must be called after genCGALRandomPolygon
def polygon_from_CGAL():
    f = open("poly.txt", "r")
    lines = f.readlines()
    polygon = Polygon([Point(0,0)]) #Empty Polygon
    points = []
    xory = 0 # x = 0 , 1 = y , 2 = both
    x = -1
    y = -1
    for line in lines:
        line = "".join(line.split()) # remove ALL whitespace
        if line != "":
            if line == "p":
                pass # ignore p's
            elif xory == 0:
                x = float(line)
                xory = 1
            elif xory == 1:
                y = float(line)
                p = Point(x,y)
                points.append(p)
                xory = 0
                x = -1
                y = -1
        else:
            print("Error from_disk(): Unknown character" + str(line))
    polygon.vertices = points
    print(polygon)
    return polygon

# Output path points which can be easily pasted in a Google Earth kml file
def export_search_path_to_kml(boundry_polygon, pathWayPoints, altitude, filename):
    build_string = "Boundry Polygon:\n"
    for v in boundry_polygon.vertices:
        build_string += str(v.x) + "," + str(v.y) + "," + str(altitude) + "\n"
    build_string += "\nSpiral Path:\n"
    for wp in pathWayPoints:
        build_string += str(wp.x) + "," + str(wp.y) + "," + str(altitude) + "\n"
    fs = open(filename, "w")
    print(build_string, file=fs)

# (INTERNAL) Reads polygon list from disk; must be called after to_disk or cgal code
def poly_list_from_disk():
    # read from file
    f = open("polyList.txt", "r")
    lines = f.readlines()
    points = []
    polygons = []
    xory = 0 # x = 0 , 1 = y , 2 = both
    x = -1
    y = -1
    for line in lines:
        line = "".join(line.split()) # remove ALL whitespace
        if line == "p":
            polygons.append(Polygon(points))
            points = []
        elif line != "":
            if xory == 0:
                x = float(line)
                xory = 1
            elif xory == 1:
                y = float(line)
                p = Point(x,y)
                points.append(p)
                xory = 0
                x = -1
                y = -1
        else:
            print("Error from_disk(): Unknown character" + str(line))
    # print(polygons)
    # print("---------------")
    return polygons

# Returns a list of 1 or more convex polygons
def getSubDivision(polygon, usePolygon = True):
    # Don't use the python polygon if it's generated in getSubDivision.cpp
    if usePolygon:
        polygon.to_disk()
    call(["./executable"]) # c++ cgal program
    return poly_list_from_disk()
# @TODO: Move polyList functions to a class
def getLeftMostPolygon(polyList):
    """Linearly searches through list of polygons for point with lowest x value.
    Returns index of polygon with that point"""
    if len(polyList) == 0:
        print("Error: Can't getLeftMostPolygon if there's no polygons")
        return None
    leftmostPoint = polyList[0].vertices[0]
    leftmostPolyIndex = 0
    for i,polygon in enumerate(polyList):
        for vert in polygon.vertices:
            if vert.x < leftmostPoint.x:
                leftmostPoint = vert
                leftmostPolyIndex = i
    return leftmostPolyIndex

def getAdjacentPolygon(polygonA, polyList):
    """Finds a polygon geometrically adjacent to polygonA"""
    for i,poly in enumerate(polyList):
        intersectPts = list(set(poly.vertices).intersection(set(polygonA.vertices)))
        if len(intersectPts) >= 2:
            return i
    print("Error: Can't find adjacent polygon")

def reorderPolygons(polyList):
    """Puts geometrically adjacent polygons next to each other in a list"""
    if len(polyList) == 0:
        print("Error: Can't reorderPolygons if there's no polygons!")
        return []
    path = []
    nextPolyIndex = getLeftMostPolygon(polyList)
    orginal_poly_count = len(polyList)
    while len(polyList) > 0:
        path.append(polyList[nextPolyIndex])
        temp = getAdjacentPolygon(polyList[nextPolyIndex], polyList)
        del polyList[nextPolyIndex]
        nextPolyIndex = temp
    if len(path) == orginal_poly_count:
        return path
    else:
        print("Error: Couldn't reorder polygons in list!")

def main():
    print("Loading the experiment parameters")
    # if true, will create a random polygon with the listed parameters
    # if false, will read a polygon from input.txt in the following format:

    createRandomPolygons = False

    # @TODO: for loop here to do 25 trials
    if createRandomPolygons == False:
        # area latitude & longitude, size of bounding box sides, vertex count
        genCGALRandomPolygon(30.5775025, -96.3511128, .001, 10)
        poly_list = getSubDivision(None, False)
    else:
        poly = polygon_from_disk()
        poly_list = getSubDivision(poly)

    print("Generating Search Path")
    poly_list = poly_list_from_disk()
    poly_list = reorderPolygons(poly_list)
    searchPath = list()
    for index, polygon in enumerate(poly_list):
        temp = polygon.getSpiralPathToCentroid(7)
        searchPath += temp
        if index < len(poly_list)-1:
            # @TODO: Modify getTransitionPathToNextPolygon to return -1 on error
            new_start_point = poly_list[index].getTransitionPathToNextPolygon(poly_list[index+1])
            # @TODO: if new_start_point == -1 then add another trial an break
            index_of_point_in_next_polygon = next( (i for i, point in enumerate(poly_list[index+1].vertices) if point == new_start_point))
            poly_list[index+1].reorderVertice(index_of_point_in_next_polygon)

    print("Exporting outputs")
    exportsMissionPlannerFile(searchPath, fileName="waypoints.txt")
    export_search_path_to_kml(polygon_from_CGAL(), searchPath, 100.0, "kmloutput.txt")

    """
    #decomposedPolygons = [polygon1, polygon2, polygon3, polygon4]
    polygon1.getSpiralPathToCentroid(3)
    new_start_point = polygon1.getTransitionPathToNextPolygon(polygon2)
    index = next( (i for i, point in enumerate(polygon2) if point == new_start_point)) # find the index of new_start_point in polygon2
    polygon2 = getReorder()
    polygon2.getSpiralPathToCentroid
    """


# Tells python to only run if called directly (not an import)
if __name__ == "__main__":
    main()
