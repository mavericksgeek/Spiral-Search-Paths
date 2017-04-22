# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
"""
def distance(A, B):
    return math.sqrt((A[0]-B[0])*(A[0]-B[0])+(A[1]-B[1])*(A[1]-B[1]))

    #get distance between two points

def midpoint(p1, p2):
    tempMid = [(p1[0]+p2[0])/2.0,(p1[1]+p2[1])/2.0]
    return tempMid
"""

"""???
def line(p1, p2):
    m=(p1[1]-p2[1])/(p1[0]-p2[0])
    b=p1[1]-(m*p1[0]) # c = y - m*x
    p3 = [m, b]
    return p3
"""
def shift(value, centroid, l2):
    bMinus = -1*value+l2[1]
    bPlus = value+l2[1]
    p1 = [0,bMinus]
    p2 = [0, bPlus]
    d1 = distance(centroid, p1)
    d2 = distance(centroid, p2)
    d1 = math.fabs((-1*l2[0]*centroid[0])+(1*centroid[1])-bMinus)/(math.sqrt(l2[0]*l2[0]+1))
    d2 = math.fabs((-1*l2[0]*centroid[0])+(1*centroid[1])-bPlus)/(math.sqrt(l2[0]*l2[0]+1))
    if(math.fabs(d1)>math.fabs(d2)):
        l2[1] = bPlus
    else:
        l2[1]=bMinus
    return l2

"""
def intersect(l1,l2):
    x = (l2[1]-l1[1])/(l1[0]-l2[0])
    y = l1[0]*x+l1[1]
    p3 = [x,y]
    return p3
"""

"""
def distanceSegment(centroid, p1, p2):
    A = centroid[0] - p1[0]
    B = centroid[1] - p1[1]
    C = p2[0] - p1[0]
    D = p2[1] - p1[1]

    dot = A * C + B * D
    len_sq = C * C + D * D
    param = -1;
    if (len_sq is not 0): #in case of 0 length line
        param = dot / len_sq
    xx = yy = 0.0
    if(param < 0):
        xx = p1[0]
        yy = p1[1]
    elif(param > 1):
        xx = p2[0]
        yy = p2[1]
    else:
        xx = p1[0] + param * C
        yy = p1[1] + param * D
    dx = centroid[0] - xx
    dy = centroid[1] - yy
    return math.sqrt(dx * dx + dy * dy)
"""


def getCircleLineIntersectionPoint(centroid, A, B, center, radius):
        baX = B[0] - A[0]
        baY = B[1] - A[1]
        caX = center[0] - A[0]
        caY = center[1] - A[1];

        a = baX * baX + baY * baY
        bBy2 = baX * caX + baY * caY
        c = caX * caX + caY * caY - radius * radius;

        pBy2 = bBy2 / a;
        q = c / a;

        disc = pBy2 * pBy2 - q;

        tmpSqrt = math.sqrt(disc)
        abScalingFactor1 = -pBy2 + tmpSqrt
        abScalingFactor2 = -pBy2 - tmpSqrt

        p1 = [A[0] - baX * abScalingFactor1, A[1]- baY * abScalingFactor1]
         # abScalingFactor1 == abScalingFactor2
        if disc is 0:
            return p1
        p2 = [A[0] - baX * abScalingFactor2, A[1] - baY * abScalingFactor2]
        #return Arrays.asList(p1, p2);
        if distance(p1,centroid) < distance(p2,centroid):
            return p1
        return p2

def printConvexSpiral(spacing,boundaryPoints):
    print 'Boundary Points'
    for point in boundaryPoints:
        print "%f , %f"%(point[0],point[1])
    print "%f , %f"%(boundaryPoints[0][0],boundaryPoints[0][1])
    print '\n'
    path = boundaryPoints
    poly = boundaryPoints
    totalX = 0
    totalY = 0
    dist = []
    for point in boundaryPoints:
         totalX += point[0]
         totalY += point[1]
    index = len(path) - 1
    boundarySize =  len(path)
    centroidLong = totalX / len(boundaryPoints)
    centroidLat = totalY / len(boundaryPoints)
    centroid = []
    xSum=0
    ySum=0
    aSum=0
    for i in range(0,len(boundaryPoints) - 1):
        xi = boundaryPoints[i][0]
        yi = boundaryPoints[i][1]
        print "%f, %f"%(xi,yi)
        xi1 = boundaryPoints[i+1][0]
        yi1 = boundaryPoints[i + 1][1]
        print "xi1 %f yi1 %f"%(xi1, yi1)
        xSum+=(xi+xi1)*(xi*yi1-xi1*yi)
        ySum+=(yi+yi1)*(xi*yi1-xi1*yi)
        aSum+=(xi*yi1-xi1*yi)
    xi=boundaryPoints[-2][0]
    yi=boundaryPoints[-2][1]
    xi1=boundaryPoints[0][0];
    yi1=boundaryPoints[0][1];
    xSum+=(xi+xi1)*(xi*yi1-xi1*yi)
    ySum+=(yi+yi1)*(xi*yi1-xi1*yi)
    aSum+=(xi*yi1-xi1*yi)
    signedArea=.5*aSum
    cX = cY = 0
    cX = 1/(6*signedArea)*xSum
    cY= 1/(6*signedArea)*ySum
    centroid = [centroidLong, centroidLat]
    newCentroid = [cX,cY]
    temp1=getCircleLineIntersectionPoint(centroid,boundaryPoints[-2],boundaryPoints[0], boundaryPoints[0], spacing) #line that was NOT drawn
    temp2=getCircleLineIntersectionPoint(centroid,boundaryPoints[1],boundaryPoints[0], boundaryPoints[0], spacing) #first drawn line
    tempMid =  midpoint(temp1,temp2)
    #find equation of line running through polygon[0] and tempMid
    slope1 = (boundaryPoints[0][1]-tempMid[1])/(boundaryPoints[0][0]-tempMid[0])
    b1 = boundaryPoints[0][1] - (slope1*boundaryPoints[0][0])
    l1=line(boundaryPoints[0],tempMid)

    #find equation parallel to the first drawn edge
    slope2 = (boundaryPoints[1][1]-temp2[1])/(boundaryPoints[1][0]-temp2[0])
    b2 = temp2[1]-(slope2*temp2[0])
    l2 = line(boundaryPoints[1],temp2)

    #shift l2 over towards the centroid
    value= math.sqrt(slope2*slope2 + 1)*spacing
    l2 = shift(value, centroid, l2)
    bMinus= -1*(math.sqrt(slope2*slope2+1)*spacing)+b2
    bPlus= math.sqrt(slope2*slope2+1)*spacing+b2
    k1 = [0, bMinus]
    k2 = [0, bPlus]
    d1=distance(centroid, k1)
    d2=distance(centroid, k2)
    b2=0.0
    if(math.fabs(d1)>math.fabs(d2)):
        b2=bPlus
    else:
        b2=bMinus

    #find the interscetion of line1 and line2
    inter=intersect(l1,l2);
    x = (b2-b1)/(slope1-slope2)
    y = slope1*x+b1
    newPoint=inter
    firstPoint=inter
    path.append(newPoint)
    dist.append(distance(path[-2],path[-3]))
    counter=len(path)
    oldL=l2
    index += 1
    #end of first calculated point
    boundarySize=len(path)
    needToFix=False
    keepGoing=True
    loopCount=0
    index=0
    polySize=len(poly)
    while(keepGoing):
        loopCount += 1
        for a in range(0,polySize):
            #since we have already added the first calculated point
            if(loopCount==1 and a==0):
                index+= 1
                oldL=l2
                poly.append(newPoint)
                continue
            else:
                #get new Line
                newL= line(path[index],path[index+1])
                index += 1
                #shift Line over
                value= math.sqrt(newL[0]*newL[0]+1)*spacing
                newL = shift(value, centroid, newL)
                #find intersection
                inter=intersect(oldL,newL)
                path.append(inter)
                oldL=newL
                if(distanceSegment(centroid,path[-1],path[-2]) < spacing):
                    keepGoing=False

    #add centroid
    path.append(centroid)
    print "Final path"
    for point in path:
        print " %f, %f"%(point[0], point[1])


def boundaryPointsdef():
    boundaryPoints = []
    boundaryPoints.append([30.577899403551037,-96.35228859798126])
    boundaryPoints.append([30.57757510639875,-96.35230783907575])
    boundaryPoints.append([30.57745845384413,-96.3518940580956])
    boundaryPoints.append([30.577606391790866,-96.3516294395307])
    boundaryPoints.append([30.577846061942093,-96.35188351790175])
    return boundaryPoints
#class Spiral:
spacing = .00004
boundaryPoints = boundaryPointsdef()
#print boundaryPoints

printConvexSpiral(spacing,boundaryPoints)
