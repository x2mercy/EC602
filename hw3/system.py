#Copyright 2017 mengxi wang wmx@bu.edu
import numpy as np

h=input()
x=input()
h=h.split()
for i in range(len(h)):
    h[i]=float(h[i])
x=x.split()
for j in range(len(x)):
    x[j]=float(x[j])
result=np.convolve(h,x)
result_list=[]
for i in range(len(result)):
    result_list.append(result[i].item())
    #while result_list[len(result_list)-1]==0 and len(result_list)>1:
#result_list.pop()
#result_list = set(result_list)
print(" ".join(str(i) for i in result_list))
