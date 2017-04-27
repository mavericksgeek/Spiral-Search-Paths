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

## examples

```python
p1 = Point(3,4) #create point by given x, y
print(p1)
p2 = Point(1,1)
print(p2)

```
# How to run the program
python main.py
