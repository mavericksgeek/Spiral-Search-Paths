import random
from modules.geometry import *
import random
import time

# def randomPolygon(pType, nVertices, nTrials):
# 
#     list2 = []
# 
#     number_of_vertices = nVertices
#     number_of_trials = nTrials
#     polygon_type = pType
#     countTrials = 0
#     
#     while True:
# 
#         time_taken = 0
#         start_time = int(round(time.time() * 1000))
#         list2 = []
# 
#         for count in range(0,number_of_vertices):
#             list_of_X = random.randrange(0,50)
#             list_of_Y = random.randrange(0,50)
#             list2.append((list_of_X,list_of_Y))
# 
#         ifConvex = checkConvex(list2)
#         
#         if ifConvex:
# 
#             if polygon_type == "convex":
# 
#                 print("Convex")
#                 end_time = int(round(time.time() * 1000))
#                 time_taken = end_time - start_time
#                 countTrials = countTrials + 1
#                 print("Trial") ,
#                 print(countTrials) ,
#                 print("Time Taken in milliseconds") ,
#                 print(time_taken) ,
#                 print(list2) 
#         else: 
# 
#             if polygon_type == "concave":
# 
#                 print("Concave")
#                 end_time = int(round(time.time() * 1000))
#                 time_taken = end_time - start_time
#                 countTrials = countTrials + 1
#                 print("Trial") ,
#                 print(countTrials) ,
#                 print("Time Taken in milliseconds") ,
#                 print(time_taken) ,
#                 print(list2)
#         
#         
#         if countTrials == number_of_trials:
#             break
#        

def randomPolygon():
    list2 = []
    number_of_vertices = random.randrange(4,10)
    for count in range(0,number_of_vertices):
        list_of_X = random.randrange(0,100)
        list_of_Y = random.randrange(0,100)
        list2.append((list_of_X,list_of_Y))
    # print(list2)
    # ifConvex = checkConvex(list2)
    # print(ifConvex)
    return Polygon(list2)

# Creates the polygon specified by selector
# DON'T CONNECT THE LAST VERTEX TO FIRST VERTEX WITH AN OVERLAPPING VERTEXl
def demoPolygon(selector):
    points = []
    if selector == 1:
        points.append(Point(0,0));
        points.append(Point(300,0));
        points.append(Point(300,200));
        points.append(Point(200,200));
        points.append(Point(200,100));
        points.append(Point(100,100));
        points.append(Point(100,200));
        points.append(Point(0,200));
    else:
        print("There's no demo polygon that corressponds with your selection.")
    return Polygon(points)

def main():
    randomPolygon()

# Tells python to only run if called directly (not an import)
if __name__ == "__main__":
    main()    
