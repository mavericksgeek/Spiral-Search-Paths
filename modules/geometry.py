from __future__ import print_function
import random
import math
from subprocess import call

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        #return "%.13f, %.13f" %(self.x, self.y)
        return "Point(%.10f, %.10f)" %(self.x, self.y)
        # return "%.13f,%.13f" %(self.y, self.x) + ",95"

    def __sub__(self, p):
        return Vector(self.x - p.x, self.y - p.y)

    def __add__(self, v):
        return Point(self.x + v.x, self.y + v.y)

    def __eq__(self, pointA):
        return self.x == pointA.x and self.y == pointA.y

    def __ne__(self, pointA):
        return self.x != pointA.x or self.y != pointA.y

    def __hash__(self):
        return hash((self.x, self.y))

    def distanceToPoint(self, pointA):
        return ( (self.x - pointA.x) ** 2 + (self.y - pointA.y) ** 2 ) ** 0.5

    def getMiddlePoint(self, pointA):
        return Point( (self.x + pointA.x)/2.0, (self.y + pointA.y)/2.0 )

    def getDistanceToSegment(self, SegmentA):
        v = SegmentA.v1
        v1 = self - SegmentA.p1
        v2 = self - SegmentA.p2

        if v.dot(v1) <= 0:
          return v1.length
        if v.dot(v2) >= 0:
          return v2.length

        return abs(v.cross(v1)/v.length)

    def isIntersectSegment(self, SegmentA):
        v1 = Vector(SegmentA.p1.x - self.x, SegmentA.p1.y - self.y)
        v2 = Vector(SegmentA.p2.x - self.x, SegmentA.p2.y - self.y)
        return v1.cross(v2) == 0 and v1.dot(v2) <= 0



class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (self.x * self.x + self.y * self.y) ** 0.5

    def __repr__(self):
        return "Vector(%.2f, %.2f)" %(self.x, self.y)

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __rsub__(self, v):
        return Vector(v.x - self.x, v.y - self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __div__(self, constant):
        return Vector(1.0* self.x/constant, 1.0*self.y/constant)

    def __mul__(self, constant):
        return Vector(self.x * constant, self.y * constant)

    def __rmul__(self, constant):
        return Vector(self.x * constant, self.y * constant)

    def dot(self, vector):
        return float(self.x * vector.x + self.y * vector.y)

    def cross(self, vector):
        return float(self.x * vector.y - self.y * vector.x)


class Segment:

    def __init__(self, pointA, pointB):
        self.p1 = pointA    #make two vertices of the line segment
        self.p2 = pointB
        self.v1 = Vector(self.p2.x - self.p1.x, self.p2.y - self.p1.y) #create two vectors for further applications
        self.v2 = -self.v1
        self.length = self.v1.length

    def __repr__(self):
        return "Segment[%s, %s]" %(self.p1, self.p2)

    def isIntersectSegment(self, SegmentA):

        c1 = (SegmentA.p1 - self.p1).cross(SegmentA.p2 - self.p1)
        c2 = (SegmentA.p1 - self.p2).cross(SegmentA.p2 - self.p2)
        c3 = (self.p1 - SegmentA.p2).cross(self.p2 - SegmentA.p2)
        c4 = (self.p1 - SegmentA.p1).cross(self.p2 - SegmentA.p1)

        if c1*c2 < 0 and c3*c4 < 0:
          return True

        if c1 == 0 and self.p1.isIntersectSegment(SegmentA):
          return True
        if c2 == 0 and self.p2.isIntersectSegment(SegmentA):
          return True
        if c3 == 0 and SegmentA.p2.isIntersectSegment(self):
          return True
        if c4 == 0 and SegmentA.p1.isIntersectSegment(self):
          return True

        return False

    def getIntersectPoint(self, segmentA):
        a = self.p2 - self.p1
        b = segmentA.p2 - segmentA.p1
        c = segmentA.p1 - self.p1

        if a.cross(b) == 0:
            return "Inf or the intersect point does not exist!"
        return self.p1 + a * (c.cross(b)/a.cross(b))



class Polygon:

    def __init__(self, list_of_points):
        """ the list of points should be in the succsessive order """
        self.vertices = list_of_points
        self.centroid = self.getCentroid()
        self.endpoint = None

    def __repr__(self):
        return "Polygon(%s)" %self.vertices

    def getCentroid(self):
        x = 0
        y = 0
        number_of_points = len(self.vertices)
        for point in self.vertices:
            x += point.x
            y += point.y
        return Point(1.0* x/number_of_points, 1.0* y/number_of_points)

    def getSpiralPathToCentroid(self, ratio):
        startPoint = self.vertices[0]
        endPoint = self.centroid
        vertices_to_centroid_vectors = list()
        spiralPath = self.vertices[:]    #list of points from outside to the centroid
        flag_number = len(self.vertices) * ratio + 1

        for point in self.vertices:
            vector = endPoint - point
            vector /= ratio
            vertices_to_centroid_vectors.append(vector)

        old_points = self.vertices[:]
        for i in range(0, ratio):
            for index,point in enumerate(old_points):
                new_point = point + vertices_to_centroid_vectors[index]
                old_points[index] = new_point
                spiralPath.append(new_point)
                if len(spiralPath) == flag_number:
                   break

        self.endpoint = spiralPath[-1] #reset the value of endpoint
        return spiralPath

    def getTransitionPathToNextPolygon(self, polygonA):
        temp = list(set(self.vertices).intersection(set(polygonA.vertices)))
        next_point = min(temp, key = lambda point: self.endpoint.distanceToPoint(point))
        return next_point

    def reorderVertice(self, index):
        self.vertices = self.vertices[index:] + self.vertices[:index]

    def getArea(self):
        temp = self.vertices[:]
        temp.append(temp[0])
        area = 0.0

        for i in range(0, len(temp)-1):
            v1 = temp[i] - Point(0.0,0.0)
            v2 = temp[i+1] - Point(0.0,0.0)
            area += v1.cross(v2)

        return abs(area)/2.0

    def isConvex(self):
        vertices = self.vertices[:]
        vertices.insert(0, vertices[-1])
        vertices.append(vertices[1])
        flag = (vertices[1] - vertices[0]).cross(vertices[2] - vertices[1])

        for i in range(0,len(vertices) - 2):
            v1 = vertices[i+1] - vertices[i]
            v2 = vertices[i+2] - vertices[i+1]
            new_sign = v1.cross(v2)
            if new_sign * flag < 0:
                return False
        return True

    def sign(x):
        if x >= 0: return 1
        else: return 0

    def checkConvex(list_of_points):
        triads=zip(list_of_points, list_of_points[1:]+[list_of_points[0]], list_of_points[2:]+[list_of_points[0]]+[list_of_points[1]])
        i = 0
        for ((x0, y0), (x1, y1), (x2,y2)) in list(triads):
            if i==0: fsign = self.sign(x2*(y1-y0)-y2*(x1-x0)+(x1-x0)*y0-(y1-y0)*x0)
            else:
                newsign = self.sign(x2*(y1-y0)-y2*(x1-x0)+(x1-x0)*y0-(y1-y0)*x0)
                if newsign != fsign: return False
            i +=1
        return True

    def to_string(self):
        string = ""
        for p in self.vertices:
            string += str(p.x) + "\n"
            string += str(p.y) + "\n"
        string += "p"
        return string

    def to_disk(self):
        f = open("poly.txt", "w")
        string = self.to_string()
        print(string, file=f)

# # @TODO: Cannot use because sides intersect (not a simple polygon)
# def getRandomPolygon(min_log, max_log, min_lat, max_lat, n_of_vertices):
#     poly = Polygon([Point(1,1)])
#     poly.vertices = list() #initilize the "blank" polygon
#     if min_log > max_log:
#         min_log, max_log = max_log, min_log
#     if min_lat > max_lat:
#         min_lat, max_lat = max_lat, min_lat
#
#     # Find number of digits of positive version
#     length_min_log = len(str(min_log).replace('-',''))
#     #length_max_log = len(str(max_log))
#     length_min_lat = len(str(min_lat).replace('-',''))
#     #length_max_lat = len(str(max_lat))
#
#     #generate number of points
#     for i in range(0, n_of_vertices):
#         log = random.randint(min_log, max_log) / (10.0 ** (length_min_log-2))
#         lat = random.randint(min_lat, max_lat) / (10.0 ** (length_min_lat-2))
#         poly.vertices.append(Point(log,lat))
#
#     #sort them in the order of counter-clockwise
#     poly.vertices = sorted(poly.vertices, key = lambda point: -math.atan2(point.y-poly.centroid.y, point.x-poly.centroid.x), reverse=True)
#
#     #Don't overlap the first and last points (remove if they overlapp)
#     print(str(poly.vertices[0]) + "==" + str(poly.vertices[-1]))
#     if poly.vertices[0] == poly.vertices[-1]:
#         del poly.vertices[-1]
#     return poly

# Helper Functions, outside of class #####################################
def getCGALRandomPolygon(lat, log, s, v):
    """Generates a random simple polygon at coordinate within a bounding square
    lat,log are the latitude and longitude (floating point)
    s is the side length of the bounding square
    v is the number of verticies in the shape"""
    # @TODO: c if true, the shape is convex, otherwise it is concave"""
    cmd = "./executable"
    cmd = cmd + " r" + str(lat)
    cmd = cmd + " v" + str(log)
    cmd = cmd + " x" + str(s)
    cmd = cmd + " y" + str(v)

    call([cmd]) # c++ cgal program



# Creates the polygon specified by selector
# DON'T CONNECT THE LAST VERTEX TO FIRST VERTEX WITH AN OVERLAPPING VERTEXl
def demoPolygon(selector):
    points = []
    # square, concave, positive, integers
    if selector == 1:
        points.append(Point(0,0));
        points.append(Point(300,0));
        points.append(Point(300,200));
        points.append(Point(200,200));
        points.append(Point(200,100));
        points.append(Point(100,100));
        points.append(Point(100,200));
        points.append(Point(0,200));
    elif selector == 2:
        # crooked, concave, negatives, and doubles
        points.append(Point(-2.2,-3));
        points.append(Point(300.55,0));
        points.append(Point(300.55,200.25));
        points.append(Point(200.25,200.25));
        points.append(Point(200.25,100));
        points.append(Point(100,100));
        points.append(Point(100,200.25));
        points.append(Point(0,200.25));
    elif selector == 3:
        points.append(Point(30.577799,-96.353317));
        points.append(Point(30.578707,-96.353378));
        points.append(Point(30.578753,-96.351288));
        points.append(Point(30.577923,-96.351219));
        points.append(Point(30.577894,-96.351845));
        points.append(Point(30.578329,-96.351959));
        points.append(Point(30.578365,-96.352837));
        points.append(Point(30.577894,-96.352768));
    else:
        print("There's no demo polygon that corressponds with your selection.")
    return Polygon(points)
