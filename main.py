            #############################################
             ### Application Programming Interface #####
              #########################################

########################################################################
### Use these common names so that we can merge code easily later.   ###
### DO NOT CHANGE THE FUNCTION NAMES, INPUTS, OR RETURN OUTPUT TYPE! ###
########################################################################

from modules.geometry import *
import randomPolygon

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
    print("Experimented Started")
    # poly = randomPolygon.demoPolygon(1)
    # poly.to_disk()
    print(poly_list_from_disk())

# Tells python to only run if called directly (not an import)
if __name__ == "__main__":
    main()
