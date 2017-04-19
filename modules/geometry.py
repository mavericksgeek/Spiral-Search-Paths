class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "Point(%.2f, %.2f)" %(self.x, self.y)

  def __sub__(self, p):
    return Vector(self.x - p.x, self.y - p.y)

  def distanceToPoint(self, pointA):
    return ( (self.x - pointA.x) ** 2 + (self.y - pointA.y) ** 2 ) ** 0.5

  def distanceToSegment(self, SegmentA):
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

  def dot(self, vector):
    return self.x * vector.x + self.y * vector.y

  def cross(self, vector):
    return self.x * vector.y - self.y * vector.x


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

class Polygon:

  def __init__(self, list_of_points):
    """ the list of points should be in the succsessive order """
    self.vertices = list_of_points

  def __repr__(self):
    return "Polygon(%s)" %self.vertices

  def checkConvex(list_of_points):
    # Sahana's code here
    # return true/false
    pass
