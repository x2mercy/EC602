// Copyright 2017 mengxi wang wmx@bu.edu
// Copyright 2017 chen rui ruirui@bu.edu
#include <vector>

using namespace std;

typedef vector<double> Poly;

// Add two polynomials, returning the result
//Poly add_poly(const Poly &a,const Poly &b);

// Multiply two polynomials, returning the result.
//Poly multiply_poly(const Poly &a,const Poly &b);

Poly add_poly(const Poly &a, const Poly &b){
    Poly c;
    for(int i=0;i<(a.size()<b.size()?a.size():b.size());i++){
        c.push_back(a[i]+b[i]);
    }
    if(a.size()>b.size()){
        c.insert(c.end(),a.begin()+b.size(),a.end());
    }else{
        c.insert(c.end(),b.begin()+a.size(),b.end());
    }
    while(c[c.size()-1]==0 && c.size()>1){
        c.pop_back();
    }
    return c;
}
Poly multiply_poly(const Poly &a,const Poly &b){
    Poly d(a.size()+b.size()-1,0);
    //    Poly d(1,0);
    for(int i=0;i<a.size();i++){
        for(int j=0;j<b.size();j++){
            d[i+j] += a[i] * b[j];
        }
    }
    while(d[d.size()-1]==0&& d.size()>1){
        
        d.pop_back();
    }
    
    return d;
}
