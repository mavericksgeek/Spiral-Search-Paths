def _getTransition(end_point, previous_polygon, current_polygon):
    #list(set(previous_polygon).intersection(current_polygon))
    edge_points = []
    for p1 in current_polygon:
        for p2 in previous_polygon:
            if p1 == p2:
                edge_points.append(p1)
    print edge_points
    distance = []
    XOrd = abs(end_point[0]) - abs(edge_points[0][0])
    YOrd = abs(end_point[1]) - abs(edge_points[0][1])
    distance.append(abs(math.sqrt((XOrd ** 2) +(YOrd ** 2))))
    XOrd = abs(end_point[0]) - abs(edge_points[1][0])
    YOrd = abs(end_point[1]) - abs(edge_points[1][1])
    distance.append(abs(math.sqrt((XOrd ** 2) + (YOrd ** 2))))
    if distance[0] > distance[1]:
        start_point = edge_points[1]
    else:
        start_point = edge_points[0]
    print start_point
    return start_point


end_point = [7,8] 
previous_polygon = [[1,2],[2,3],[3,4],[3,9]]
current_polygon = [[1,2],[4,3],[5,6],[2,3]]



_getTransition(end_point, previous_polygon, current_polygon)
