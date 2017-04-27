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
#include <cassert>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <time.h>

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef Polygon_2::Vertex_iterator                          Vertex_iterator;
typedef std::list<Polygon_2>                                Polygon_list;
typedef CGAL::Creator_uniform_2<int, Point_2>               Creator;
typedef CGAL::Random_points_in_square_2<Point_2, Creator>   Point_generator;

// Writes a list of polygons to the disk
void poly_list_to_disk(Polygon_list* pl){
  std::ofstream f;
  f.std::ofstream::open("polyList.txt", std::ofstream::out);
  std::string poly_list = "";
  // loop through polygons
   for(std::list<Polygon_2>::iterator p = pl->begin(); p != pl->end(); ++p){
     // loop through vertcies of polygon
    for(Vertex_iterator v = p->vertices_begin(); v != p->vertices_end(); ++v){
      f << v->x() << "\n";
      f << v->y() << "\n";
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
    int x = -1;
    int y = -1;
    for (size_t i = 0; i < lines.size(); i++) {
      if (lines[i] == "p"){
        break;
      }
      else if (lines[i] != ""){
      }
          if (xory == 0){
            x = atof(lines[i].c_str());
            xory = 1;
          }
          else if (xory == 1){
            y = atof(lines[i].c_str());
            xory = 2;
          }
          else if (xory == 2){
            polygon.push_back(Point_2(x,y));
            x = -1;
            y = -1;
            xory = 0;
          }
      else{
        std::cout << "Error from_disk(): Unknown char in poly.txt\n";
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
int main(int argc, char** args)
{
   Polygon_2    polygon;
   Polygon_list partition_polys;
	
  polygon = from_disk();
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
