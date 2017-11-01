// Copyright 2017 mengxi wang wmx@bu.edu
// Copyright 2017 rui chen ruirui@bu.edu
#include <iostream>
#include <ctime>
#include <math.h>
using namespace std;

int main()
{
	clock_t start_clock,end_clock;	
	
	uint16_t j=1;
	
	start_clock = clock();  // Timing starts here
	while(j>0) 
	{
		 j++;
	}
	end_clock = clock();    // Timing stops here
	double second1 = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;
	std::cout << "estimated in8 time (nanoseconds): "
    		<< second1*pow(10,9)/(pow(2,8) << std::endl;
    std::cout << " measured int16 time (microseconds): "
            << second1*pow(10,6) << std::endl;
    
    std::cout << "estimated int32 time (seconds): "
            << second1*((pow(2,32)/(pow(2,16)) << std::endl;
    std::cout << "estimated int64 time (years): "
            << second1*((pow(2,64)/(pow(2,16))/(24*3600*365) << std::endl;
}