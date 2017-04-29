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

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef Polygon_2::Vertex_iterator                          Vertex_iterator;
typedef std::list<Point_2>::iterator                        Point_Iter;
typedef std::list<Polygon_2>                                Polygon_list;
typedef CGAL::Creator_uniform_2<int, Point_2>               Creator;
typedef CGAL::Random_points_in_square_2<Point_2, Creator>   Point_generator;


// Creates polygon with <= number_vertecies
  // all points are radius distance coordinate point
  // Stores polygon in poly_buff and convex/concave in isConvex
void random_poly(double radius, int number_vertecies, Point_2 coordinate,
   const Polygon_2* poly_buff){
  Polygon_2            polygon;
  std::list<Point_2>   point_set;

  int size = number_vertecies;
  // copy size points from the generator, eliminating duplicates, so the
  // polygon will have <= size vertices
  CGAL::copy_n_unique(Point_generator(radius), size,
                     std::back_inserter(point_set));
  //// Print random points
  // std::ostream_iterator< Point_2 >  out( std::cout, " " );
  // std::cout << "From the following " << point_set.size() << " points "
          //  << std::endl;
  // std::copy(point_set.begin(), point_set.end(), out);
  // std::cout << std::endl;
  // Move polygon near coordinate by translating all points
  int x,y = 0;
  for(Point_Iter it = point_set.begin(); it != point_set.end(); ++it ){
    x = it->x() + coordinate.x();
    y = it->y() + coordinate.y();
    Point_2 temp(x,y);
    *it = temp;
  }
  
  // Turn points into a polygon
  CGAL::random_polygon_2(point_set.size(), std::back_inserter(polygon),
                        point_set.begin());

  // std::cout << "The following simple polygon was made: " << std::endl;
  std::cout << polygon << std::endl;
}

// Writes a list of polygons to the disk
void poly_list_to_disk(Polygon_list* pl){
  std::ofstream f;
  f.std::ofstream::open("polyList.txt", std::ofstream::out);
  std::string poly_list = "";
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

// Prints polygon in svg format
// std::string svg_poly(Polygon_2& polygon, std::string stroke_color, std::string fill_color){
//   std::string body = "";
// 	body += "<polygon points=\"";
// 	for(Vertex_iterator it = polygon.vertices_begin(); it != polygon.vertices_end(); ++it){
//  //@TODO: Solve later
// 		// body += std::to_string(it->x()) + "," + std::to_string(it->y()) + " ";
// 	}
// 	body += "\" style=\"fill:" + fill_color + "; stroke:" + stroke_color + 
// 	"stroke-width:1\" />" + "\n";
//   return body;
// }

// Converts a polygon list into an svg string
// void to_svg(Polygon_list pl){
//   std::string body ="";
//   std::string path = "logs/out.svg";
//   std::ofstream f(path.c_str());
//   for(std::list<Polygon_2>::iterator it = pl.begin(); it != pl.end(); ++it){
//     body += svg_poly(*it, "white", "blue");
//   }
// 	f << "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">" << '\n';
// 	f << body << '\n';
// 	f << "</svg>" << '\n';
// }

// @TODO: Output as list of x y points counter clockwise	
// @TODO: Log data
int main(int argc, char** argv)
{
  // Init
   Polygon_2    polygon;
   Polygon_list partition_polys;
   Point_2 coordinate;
   int x = 10;
   int y = 10;
   int radius = 10;
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
         x = atoi(optarg);
         break;
     case 'y':
         y = atoi(optarg);
         break;
     case 'r':
        radius = atoi(optarg);
        break;
     case 'v':
        max_verticies = atoi(optarg);
        break;
       default:
   std::cerr << "Invalid Command Line Argument\n";
   }
  }
  coordinate = Point_2(x,y);
  polygon = from_disk();
  // std::cout << "Polygon:\n" << polygon << '\n';
  
  // random_poly(radius, max_verticies, coordinate, &polygon);
  //Hertel Melhorn (Do not connect the last line)
   CGAL::approx_convex_partition_2(polygon.vertices_begin(),
                                   polygon.vertices_end(),
                                   std::back_inserter(partition_polys));
                                   
   assert(CGAL::convex_partition_is_valid_2(polygon.vertices_begin(),
                                            polygon.vertices_end(),
                                            partition_polys.begin(),
                                            partition_polys.end()));
  poly_list_to_disk(&partition_polys);
  return 0;
}
