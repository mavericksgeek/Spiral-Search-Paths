            #############################################
             ### Application Programming Interface #####
              #########################################

########################################################################
### Use these common names so that we can merge code easily later.   ###
### DO NOT CHANGE THE FUNCTION NAMES, INPUTS, OR RETURN OUTPUT TYPE! ###
########################################################################

from modules.geometry import *
from modules.export import *
from subprocess import call

## Function ##############################################


# Generates a random polygon for testing of the other functions
# def _getRandomPolygon():
  # return polygon
  # pass

# Takes in boundry polygon and returns list of convex_polygon
# def _getSubDivision(concave_polygon):
  # if checkConvex(concave_polygon):
 #  	return concave_polygon
  # send_to_cgal(concave_polygon)
  # list_of_polygons = read_back_cgal()

  # polygon will need to be in ccw order
  # see if polygons can be returned an order

  # return list_of_polygons
  # pass

# Takes in a list of spirals and a boundry polygon
# Returns a list of segments which are the transitions between spiral endpoints
# def _getTransitionPath(boundary_polygon, list_of_spirals):
  # return list_of_line_segments
  # pass

# Takes in a convex polygon and returns a spiral which fits inside
# def _getSpiralPath(convex_polygon):
  # return spiral
  # pass

# Converts a list of points to a list of svg lines;
# use by redirecting output to x.svg file
def search_path_to_svg(search_path):
    lines = []
    line = ""
    lp = None # last point
    first = True
    print(search_path)
    # print("<svg>\n")
    for p in search_path:
        if not first:
            line += "<line "
            line +=" x1=" + str(lp.x) +" y1=" + str(lp.y) +" x2=" + str(p.x) +" y2=" + str(p.y)
            line += " style=\"stroke:rgb(255,0,0);stroke-width:2\" />"
            print(line)
        line = ""
        lp = p
        first = False
    # print("\n</svg>\n")


# Reads polygon list from disk; must be called after to_disk or cgal code
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
def getSubDivision(polygon):
    polygon.to_disk()
    call(["./executable"]) # c++ cgal program
    return poly_list_from_disk()

def main():
    print("Experimented Started")
    poly = demoPolygon(1)
    # poly = getRandomPolygon(-963514029, -963511128, 305775025, 305778213, 5)
    poly_list = getSubDivision(poly)
    poly_list = poly_list_from_disk()
    print(poly_list)
    print("Polygon List")
    result = list()

    for index, polygon in enumerate(poly_list):
        temp = polygon.getSpiralPathToCentroid(3)
        result += temp
        if index < len(poly_list)-1:
            new_start_point = poly_list[index].getTransitionPathToNextPolygon(poly_list[index+1])
            index_of_point_in_next_polygon = next( (i for i, point in enumerate(poly_list[index+1].vertices) if point == new_start_point))
            poly_list[index+1].reorderVertice(index_of_point_in_next_polygon)

        print("centroid:",polygon.centroid)

    print(result)

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
