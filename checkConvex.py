import random
def sign(x):
    if x >= 0: return 1
    else: return 0
def checkConvex(list_of_points):
    triads=zip(list_of_points, list_of_points[1:]+[list_of_points[0]], list_of_points[2:]+[list_of_points[0]]+[list_of_points[1]])
    i = 0
    for ((x0, y0), (x1, y1), (x2,y2)) in list(triads):
        if i==0: fsign = sign(x2*(y1-y0)-y2*(x1-x0)+(x1-x0)*y0-(y1-y0)*x0)
        else:
            newsign = sign(x2*(y1-y0)-y2*(x1-x0)+(x1-x0)*y0-(y1-y0)*x0)
            if newsign != fsign: return False
        i +=1
    return True

def randomPolygon():
    list2 = []
    number_of_vertices = random.randrange(4,10)
    for count in range(0,number_of_vertices):
        list_of_X = random.randrange(0,100)
        list_of_Y = random.randrange(0,100)
        list2.append((list_of_X,list_of_Y))
    print(list2)
    ifConvex = checkConvex(list2)
    print(ifConvex)

    
randomPolygon()
