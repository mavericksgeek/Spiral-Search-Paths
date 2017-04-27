            #############################################
             ### Application Programming Interface #####
              #########################################

########################################################################
### Use these common names so that we can merge code easily later.   ###
### DO NOT CHANGE THE FUNCTION NAMES, INPUTS, OR RETURN OUTPUT TYPE! ###
########################################################################

from modules.geometry import *
import randomPolygon
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
    xory = 0 # x = x , 1 = y , 2 = both
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
                xory = 2
            elif xory == 2:
                p = Point(x,y)
                points.append(p)
                x = -1
                y = -1
                xory = 0
        else:
            print("Error from_disk(): Unknown char in poly.txt")
    return polygons

def main():
    # print("Experimented Started")
    poly = randomPolygon.demoPolygon(1)
    poly.to_disk()
    call(["./executable"]) # c++ cgal program
    poly_list = poly_list_from_disk()
    searchpath = []
    last_polygon = None
    # Take each polygon
    for poly in poly_list:
        searchpath += poly.getSpiralPathToCentroid(2)
        if last_polygon != None:
            searchpath += poly.getTransitionPathToNextPolygon(last_polygon)
    print(searchpath)
    print(search_path_to_svg(searchpath))

# Tells python to only run if called directly (not an import)
if __name__ == "__main__":
    main()
