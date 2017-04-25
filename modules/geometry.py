from __future__ import print_function
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "%.13f, %.13f" %(self.x, self.y)
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
        return string

    def to_disk(self):
        f = open("poly.txt", "w")
        string = self.to_string()
        print(string, file=f)
