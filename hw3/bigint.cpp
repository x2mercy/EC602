// Copyright 2017 mengxi wang wmx@bu.edu
#include <string>
#include <vector>
using namespace std;

typedef string BigInt;
typedef vector<double> Poly;
//BigInt multiply_int(const BigInt &a,const BigInt &b);
//Poly multiply_Poly(const Poly &a, const Poly &b);
//Poly BigInt_P(const BigInt &a);
//Poly Poly_deci(const Poly &a);
//BigInt Poly_BigInt(const Poly &a);

BigInt multiply_int(const BigInt &a,const BigInt &b){
    int d;
    BigInt result_BI;
    d=a.size()+b.size();
    vector<int> result,temp;
    if(a=="0"||b=="0"){
        return "0";
    }
    for(int i = 0; i<d;i++)
    {
        result.push_back(0);
    }
    for(int i = 0; i<b.size()+1;i++)
    {
        temp.push_back(0);
    }
    for(int i= a.size()-1; i>=0;i--)
    {
        for (int j = b.size()-1; j>=0;j--)
        {
            temp[j+1] += (int)(b[j]-'0')* (a[i]-'0');
            if (temp[j+1]>9)
            {
                int next = temp[j+1];
                temp[j+1]=next%10;
                temp[j] +=next/10;
            }
        }
        int index = b.size()+i;
        for (int k = temp.size()-1;k>=0;k--)
        {
            result[index-temp.size()+k+1]+=temp[k];
            if(result[index-temp.size()+k+1]>9)
            {
                int next = result[index-temp.size()+k+1];
                result[index-temp.size()+k+1]=next%10;
                result[index-temp.size()+k]+=next/10;
            }
        }
        for (int i =0; i<temp.size();i++)
        {
            temp[i]=0;
        }
        
    }
    if(result[0]==0)
    {
        result.erase(result.begin());
    }
    for (int i = 0; i<result.size();i++)
    {
        result_BI+=to_string(result[i]);
    }
    return result_BI;
}
    
