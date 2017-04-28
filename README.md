# spiralSearchPaths
Generates spiral search paths for concave free space

## Set Up
Most functions are accessible through the geometry module. You can use it with:
```python
from modules.geometry import *
```

Part of the system uses the c++ CGAL library which can be installed and used as follows:

Install CGAL: http://www.cgal.org/download/linux.html

CGAL Tutorial: http://doc.cgal.org/latest/Partition_2/index.html

How to build a CGAL program:
```
cd /path/to/your_program.cpp
cgal_create_CMakeLists -s executable
cmake -DCGAL_DIR=$HOME/CGAL-4.9.1 .
make
```

## API Reference
### Exports waypoints
To generate the txt file which will be used in MAVProxy, you should firstly import the module:
```python
from modules.export import *
```
And try to run this with your list of points and file name:
```python
createWaypointFile(list_of_waypoints, fileName="waypoints.txt")
```

### Generate Random Polygon
To generate a random polygon, you should include geometry module first:
```python
from modules.geometry import *
```
Then, you can use the function getRandomPolygon:
```python
getRandomPolygon(min_log, max_log, min_lat, max_lat, n_of_vertices)
```
Note that you the input longitude and latitude should not be a float, you should input a int instead. 
If you want to get a random polygon boundary (with 5 vertices) around the lake at College Station, 
for example, the longitute is about -96.3511128 to -96.3514029 and the latitude is about 30.5775025 to 30.5778213, 
then you can write as follows:
```python
getRandomPolygon(-963514029, -963511128, 305775025, 30.5778213, 5)
```

## examples

```python
p1 = Point(3,4) #create point by given x, y
print(p1)
p2 = Point(1,1)
print(p2)

```
# How to run the program
python main.py
