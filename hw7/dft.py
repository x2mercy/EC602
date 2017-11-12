#Copyright 2017 mengxi wang wmx@bu.edu
#Copyright 2017 rui chen ruirui@bu.edu
from numpy import zeros, exp, array, pi

def DFT(x):
    if type(x)==dict:
        raise ValueError
    try:
        N = len(x)
        X = zeros(N, dtype="complex")
        for k in range(0,N):
            for i in range(len(x)):
                X[k]+=x[i]*exp(-2j*pi*i*k/N)
        return array(X)
    except:
        raise ValueError
    
def main():
    x_input=[1,2,3]
    X=DFT(x_input)
    print("x:",x_input)
    print("X:",X)
    
if __name__ == '__main__':
    main()