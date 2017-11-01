// Copyright 2017 mengxi wang wmx@bu.edu
#include <iostream>
int main(int argumentcount,char **arguments){
	char *a;
	int i;
	for(i=1;i<5;i++){
		a=arguments[i];
		std::cout << a << '\n';
	}
	for(i=5;i<argumentcount;i++){
		a=arguments[i];
		std::cerr << a << '\n';
	}
	
	return 0;
}