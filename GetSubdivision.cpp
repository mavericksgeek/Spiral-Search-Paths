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

typedef CGAL::Exact_predicates_inexact_constructions_kernel K;
typedef CGAL::Partition_traits_2<K>                         Traits;
typedef Traits::Point_2                                     Point_2;
typedef Traits::Polygon_2                                   Polygon_2;
typedef Polygon_2::Vertex_iterator                          Vertex_iterator;
typedef std::list<Polygon_2>                                Polygon_list;
typedef CGAL::Creator_uniform_2<int, Point_2>               Creator;
typedef CGAL::Random_points_in_square_2<Point_2, Creator>   Point_generator;

void make_test_polygon(Polygon_2& polygon)
{
	// Must be Counter clockwise
	// polygon.push_back(Point_2(0,0));
	// polygon.push_back(Point_2(300,0));
	// polygon.push_back(Point_2(300,200));
	// polygon.push_back(Point_2(200,200));
	// polygon.push_back(Point_2(200,100));
	// polygon.push_back(Point_2(100,100));
	// polygon.push_back(Point_2(100,200));
	// polygon.push_back(Point_2(0,200));
	// polygon.push_back(Point_2(0,0));

	
}

// Prints polygon in svg format
void print_poly(Polygon_2& polygon, std::string stroke_color, std::string fill_color){
	std::cout << "<polygon points=\"";
	for(Vertex_iterator it = polygon.vertices_begin(); it != polygon.vertices_end(); ++it){
		std::cout << it->x() << "," << it->y() << " ";
	}
	std::cout << "\" " << "style=\"fill:" << fill_color << ";stroke:" << stroke_color << 
	"stroke-width:1\" />" << '\n';
}

void print_svg(std::string body){
	std::cout << "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">" << '\n';
	std::cout << body << '\n';
	std::cout << "</svg>" << '\n';
}

// @TODO: Output as list of x y points counter clockwise	
int main(int argc, char** args)
{
   Polygon_2    polygon;
   Polygon_list partition_polys;
													
   make_test_polygon(polygon);
	 print_poly(polygon, "white", "red");
	 std::cout << "-------------------" << '\n';
   CGAL::approx_convex_partition_2(polygon.vertices_begin(),
                                   polygon.vertices_end(),
                                   std::back_inserter(partition_polys));

   assert(CGAL::convex_partition_is_valid_2(polygon.vertices_begin(),
                                            polygon.vertices_end(),
                                            partition_polys.begin(),
                                            partition_polys.end()));

	 for(std::list<Polygon_2>::iterator it = partition_polys.begin(); it != partition_polys.end(); ++it){
		 print_poly(*it, "white", "blue");
	 }
   return 0;
}
