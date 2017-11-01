#Copyright 2017 mengxi wang wmx@bu.edu
class Polynomial():
    def __init__(self, input=[]):
        self.Poly={}
        for i in range(len(input)):
            exp=len(input)-1-i
            if input[i]!=0:
                self.Poly[exp]=input[i]
    
    def __add__(self,adder):
        result=Polynomial()
        result.Poly=self.Poly.copy()
        for i in adder.Poly.keys():
            if i in result.Poly.keys():
                result.Poly[i]+=adder.Poly[i]
            else:
                result.Poly[i]=adder.Poly[i]
        for i in result.Poly.keys():
            if result.Poly[i]==0:
                result.Poly.pop(i)
        return result
    def __sub__(self,sub):
        result=Polynomial()
        result.Poly=self.Poly.copy()
        for i in sub.Poly.keys():
            if i in result.Poly.keys():
                result.Poly[i]-=sub.Poly[i]
            else:
                result.Poly[i]=-sub.Poly[i]
        for i in result.Poly.keys():
            if result.Poly[i]==0:
                result.pop(i)
        return result

	

    def __mul__(self,mul):
        result=Polynomial()
       # result.Poly=self.Poly.copy()
        for exp in self.Poly.keys():
            for exp2 in mul.Poly.keys():
                if (exp+exp2) in result.Poly:
                    result.Poly[exp+exp2]+=self.Poly[exp]*mul.Poly[exp2]
                else:
                    result.Poly[exp+exp2]=self.Poly[exp]*mul.Poly[exp2]
                
            
   #     for i in result.Polykeys():
    #        if result.Poly[i]==0:
     #           result.pop(i)
        return result

    def __eq__(self,b):
        return self.Poly==b.Poly

    def eval(self,x):
        result=0
        for exp in self.Poly.keys():
            result+=self.Poly.get(exp)*(x**exp)
        return result

    def deriv(self):
        result=Polynomial()
        for exp in self.Poly.keys():
            if(exp!=0):
                result.Poly[exp-1]=self.Poly[exp]*exp
 #           else:
  #              result.Poly[exp]=0
        return result
    
    def __setitem__(self,exp,coeff):
        if coeff!=0:
            self.Poly[exp]=coeff
        else:
            self.Poly[exp]=0
    
    def __getitem__(self,exp):
        if exp in self.Poly:
            return self.Poly[exp]
        else:
            return 0
