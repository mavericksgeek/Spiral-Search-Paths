// Install CGAL: http://www.cgal.org/download/linux.html
// Tutorial: http://doc.cgal.org/latest/Partition_2/index.html
// cd /path/to/program
// cgal_create_CMakeLists -s executable
// cmake -DCGAL_DIR=$HOME/CGAL-4.9.1 .
// make

#include <CGAL/Exact_predicates_inexact_constructions_kernel.h>
#include <CGAL/Partition_traits_2.h>
#include <CGAL/partition_2.h>
#include <CGAL/point_generators_2.h>
#include <CGAL/random_polygon_2.h>
#include <CGAL/Simple_cartesian.h>
#include <CGAL/Polygon_2.h>
#include <CGAL/Random.h>
#include <CGAL/algorithm.h>
#include <cassert>
#include <list>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <time.h>
// #ifdef CGAL_USE_GMP
// #include <CGAL/Gmpz.h>
// typedef CGAL::Gmpz RT;
// #else
// NOTE: the choice of double here for a number type may cause problems
//       for degenerate point sets
#include <CGAL/double.h>
typedef double RT;
// #endif

// These are for decomposition
typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef Polygon_2::Vertex_iterator                          Vertex_iterator;
typedef std::list<Point_2>::iterator                        Point_Iter;
typedef std::list<Polygon_2>                                Polygon_list;
typedef CGAL::Creator_uniform_2<int, Point_2>               Creator;
typedef CGAL::Random_points_in_square_2<Point_2, Creator>   Point_generator;
// These are for random_poly
typedef K::Point_2                                           RPoint_2;
typedef std::list<Point_2>                                   RContainer;
typedef CGAL::Polygon_2<K, RContainer>                       RPolygon_2;
typedef CGAL::Random_points_in_square_2< RPoint_2 >          RPoint_generator;

// Creates polygon with <= number_vertecies
  // all points are radius distance coordinate point
  // Stores polygon in poly_buff and convex/concave in isConvex
Polygon_2 random_poly(double radius, int number_vertecies, Point_2 coordinate){
    RPolygon_2            polygon;
    std::list<RPoint_2>   point_set;
    CGAL::Random         rand;


    // create n-gon and write it into a window:
    CGAL::random_polygon_2(number_vertecies, std::back_inserter(polygon),
                           RPoint_generator(radius));

     // Translate the points to the provided coordinate
     for (std::list<Point_2>::iterator it = polygon.vertices_begin(); it != polygon.vertices_end(); ++it) {
       *it = Point_2(it->x() + coordinate.x(), it->y() + coordinate.y());
     }

    std::cout << "The following simple polygon was made: " << std::endl;
    std::cout << polygon << std::endl;
    return polygon;
}

// Writes a list of polygons to the disk
void poly_list_to_disk(Polygon_list* pl){
  std::ofstream f;
  f.std::ofstream::open("polyList.txt", std::ofstream::out);
  // loop through polygons
   for(std::list<Polygon_2>::iterator p = pl->begin(); p != pl->end(); ++p){
     // loop through vertcies of polygon
    for(Vertex_iterator v = p->vertices_begin(); v != p->vertices_end(); ++v){
      f << std::fixed << std::setprecision(8) << v->x() << "\n";
      f << std::fixed << std::setprecision(8) << v->y() << "\n";
    }
      f << "p\n";
	 }
}

// Writes a CGAL polygon to the poly.txt file for python to read
void poly_to_disk(Polygon_2* p){
    std::ofstream f;
    f.std::ofstream::open("poly.txt", std::ofstream::out);
    // loop through vertcies of polygon
   for(Vertex_iterator v = p->vertices_begin(); v != p->vertices_end(); ++v){
     f << std::fixed << std::setprecision(8) << v->x() << "\n";
     f << std::fixed << std::setprecision(8) << v->y() << "\n";
   }
}
// # Reads polygon list from disk; must be called after to_disk or cgal code
Polygon_2 from_disk(){
    //# read from file
    std::ifstream f;
    f.std::ifstream::open("poly.txt", std::ifstream::in);
    std::vector<std::string> lines;
    std::string l;
    while (std::getline(f,l)) {
      lines.push_back(l);
      // std::cout << l << '\n'; // print what is read
    }
    Polygon_2 polygon;
    int xory = 0; //# x = x , 1 = y , 2 = both
    double x = -1;
    double y = -1;
    for (size_t i = 0; i < lines.size(); i++) {
      if (lines[i] == "p"){
        break;
      }
      else if (lines[i] != ""){
      }
          if (xory == 0){
            // std::cout << "StrX:" << lines[i].c_str() << '\n';
            x = atof(lines[i].c_str());
            // std::cout << "x:" << x << '\n';
            xory = 1;
          }
          else if (xory == 1){
            // std::cout << "StrY:" << lines[i].c_str() << '\n';
            y = atof(lines[i].c_str());
            // std::cout << "y:" << y << '\n';
            polygon.push_back(Point_2(x,y));
            x = -1;
            y = -1;
            xory = 0;
          }
      else{
        std::cout << "Error from_disk(): Unknown character " << lines[i] << std::endl;
      }
    }
    f.close();
    return polygon;
}

void make_test_polygon(Polygon_2& polygon)
{
	// Must be Counter clockwise
	polygon.push_back(Point_2(0,0));
	polygon.push_back(Point_2(300,0));
	polygon.push_back(Point_2(300,200));
	polygon.push_back(Point_2(200,200));
	polygon.push_back(Point_2(200,100));
	polygon.push_back(Point_2(100,100));
	polygon.push_back(Point_2(100,200));
	polygon.push_back(Point_2(0,200));
	polygon.push_back(Point_2(0,0));


}


// @TODO: Output as list of x y points counter clockwise
// @TODO: Log data
int main(int argc, char** argv)
{
  // std::cout << "Enter CGAL-----------------------------" << '\n';
  // Init
   Polygon_2    polygon;
   Polygon_list partition_polys;
   Point_2 coordinate;
   double x = 10;
   double y = 10;
   double radius = 10;
   int max_verticies = 10;
	 bool isConvex = false;
   //
  // Parses options that start with '-' and adding ':' makes an arg mandontory
  // r - double radius
  // v - int number_vertecies
  // x - Point_2 coordinate x
  // y - Point_2 coordinate y
  int opt = 0;
  while ((opt = getopt(argc, argv, "r:v:x:y:")) != -1){
   switch(opt) {
     case 'x':
         x = atof(optarg);
         break;
     case 'y':
         y = atof(optarg);
         break;
     case 'r':
        radius = atof(optarg);
        break;
     case 'v':
        max_verticies = atoi(optarg);
        break;
       default:
   std::cerr << "Invalid Command Line Argument\n";
   }
  }
  coordinate = Point_2(x,y);

  // Generate a random polygon if the args provided.
  // Otherwise try to decompose the polygon in the poly.txt file
  if (argc == 9){
    std::cout << "Creating random polygon" << '\n';
    polygon = random_poly(radius, max_verticies, coordinate);
    poly_to_disk(&polygon);
  }
  else if (argc == 1){
    std::cout << "Decomposing polygon from disk" << '\n';
    polygon = from_disk();
    // std::cout << "Polygon in CGAL:\n" << polygon << '\n';
    //Hertel Melhorn (Do not overlap lines or points!!!!!!!!!!!!)
    CGAL::approx_convex_partition_2(polygon.vertices_begin(),
    polygon.vertices_end(),
    std::back_inserter(partition_polys));

    assert(CGAL::convex_partition_is_valid_2(polygon.vertices_begin(),
    polygon.vertices_end(),
    partition_polys.begin(),
    partition_polys.end()));
    poly_list_to_disk(&partition_polys);
  }
  else{
    std::cout << "Invalid Command Line Arguments to CGAL" << '\n';
      std::cout << "CGAL: " << x << " " << y << " " << radius << " " << max_verticies << " " << std::endl;
  }
    // std::cout << "Exit CGAL-----------------------------" << '\n';
    return 0;
}
