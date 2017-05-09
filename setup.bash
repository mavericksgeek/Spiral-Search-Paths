# Installation ###############################################################
# The following will install mission planner and cgal

# # Install CGAL
sudo apt-get install libcgal-dev; # install the CGAL library
sudo apt-get install libcgal-demo; # install the CGAL demos
#
# # Install SITL http://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html
python --version; # Python should already be installed on ubuntu
sudo apt-get install python-pip;
sudo pip install dronekit-sitl -UI;
dronekit-sitl rover-2.50;
echo "Kill this once you see: Waiting for TCP connection"
#
# # Mavproxy intall http://ardupilot.github.io/MAVProxy/html/getting_started/download_and_installation.html
sudo apt-get install python-dev python-opencv python-wxgtk3.0 python-pip python-matplotlib python-pygame python-lxml;
sudo pip install MAVProxy;
#
# # Install Mission planner/Ground Station
# # Note the instructions are wrong, you must use wxgtk3.0
sudo apt-get install python-matplotlib python-serial python-wxgtk3.0 python-wxtools python-lxml;
sudo apt-get install python-scipy python-opencv ccache gawk git python-pip python-pexpect;
sudo pip install future pymavlink MAVProxy;
git clone git://github.com/ArduPilot/ardupilot.git;
cd ardupilot;
git submodule update --init --recursive;

echo ""
echo "Configuration----------------------------------------------------"
echo "Mission Planner Configuration"
export PATH=$PATH:$HOME/ardupilot/Tools/autotest;
export PATH=/usr/lib/ccache:$PATH;
. ~/.bashrc;
cd ardupilot/APMrover2;
echo "Add the following to /home/YourUserName/ardupilot/Tools/autotest/location.txt"
echo "CollegeStation=30.57782135288359,-96.35111282486872,50,305"

echo ""
echo "CGAL Configuration and Compilation:"
echo "Go to https://cmake.org/download/ to install cmake";
echo "After install cmake, go to your program and enter this into the terminal:"
echo "cd /path/to/YourProgram "
echo "cgal_create_CMakeLists -s executable "
echo "cmake -DCGAL_DIR=$HOME/CGAL-4.9.1 . "
echo "make"

echo ""
echo "How to run everything:---------------------------------------------------"
echo "Running Mission Planning"
echo "This command clears previous settings"
echo "sim_vehicle.py -w"
echo "You have two options when running the ground station:"
echo "A) Load a specfic location"
echo "sim_vehicle.py -j4 -L CollegeStation --console --map test"
echo "B) Load the default location"
echo "sim_vehicle.py --console --map test"
echo ""
echo "After starting mission planner, enter the follow to automatically test"
echo "arm throttle"
echo "auto mode"
