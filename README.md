# driver-rider-simulation
Simulate an application in which users who are a rider on a co-ordinate based map can request for a driver to take them 
to their desired destination the map. A text file called "events.txt" lists several events (one per line) that
occur during the course of a simulation. Riders are at co-ordinate (x,y) origin and wish to get to co-ordinate destination, 
and drivers try to fulfill these requests within the patience factor of riders. Drivers travel at a certain speed on the map.
The program will record the distance travelled by drivers with and without a rider, the time, and in the console print the 
average distance travelled by drivers and the average time taken.

Currently a MemoryError is raised when running the program with the "events.txt" file.
