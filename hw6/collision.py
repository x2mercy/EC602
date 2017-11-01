#!/usr/bin/env python
# Copyright 2017 Mengxi Wang wmx@bu.edu
# -*- coding: utf-8 -*-

import numpy
import sys
import math
import os
import copy

balls_ori=[]
target_ori=[]

def collision_time(balls):
    time=[]
    for i in range(len(balls)):
        for j in range(i,len(balls)):
            if i==j:
                continue
            balls[i][1]=float(balls[i][1])
            balls[i][2]=float(balls[i][2])
            balls[i][3]=float(balls[i][3])
            balls[i][4]=float(balls[i][4])
            balls[j][1]=float(balls[j][1])
            balls[j][2]=float(balls[j][2])
            balls[j][3]=float(balls[j][3])
            balls[j][4]=float(balls[j][4])
            delta_x = balls[i][1] - balls[j][1]
            delta_y = balls[i][2] - balls[j][2]
            delta_vx = balls[i][3] - balls[j][3]
            delta_vy = balls[i][4] - balls[j][4]
            a=delta_vx*delta_vx + delta_vy*delta_vy
            b=delta_x*delta_vx*2+delta_y*delta_vy*2
            c=delta_x*delta_x+delta_y*delta_y-100
            delta = b*b-a*c*4
            if delta<=0:
                continue
            elif delta>0:
                t1=(-b+delta**0.5)/(2*a)
                t2=(-b-delta**0.5)/(2*a)
                if t1*t2<0:
                    time.append([max(t1,t2),balls[i][0],balls[j][0]])
                elif t1*t2==0:
                    continue
                elif t1<0 and t2<0:
                    continue
                else:
                    time.append([min(t1,t2),balls[i][0],balls[j][0]])
                
    if len(time)==0:
        return -1
    else:
        time.sort()        
        if time[0][0]==0 and time[1][0]==0:
            min_time=time[1]
        else:
            min_time=time[0]
        return min_time
    
    

def select_time(k,balls,target):
    if len(balls)==1:
        balls[0][1]=update_x_one(balls,target,k)
        balls[0][2]=update_y_one(balls,target,k)
        balls[0][3]=float(balls[0][3])
        balls[0][4]=float(balls[0][4])
    else:

        min_time=collision_time(balls)

        if min_time==-1:
            for i in range(len(balls)):  
                balls[i][1]=update_x_nocol_(balls,target,k,i)
                balls[i][2]=update_y_nocol_(balls,target,k,i)
            
        elif float(target[k])<min_time[0] or min_time[0]<9e-15 or min_time[0]==0:
            for i in range(len(balls)):  
                balls[i][1]=update_x_nocol_(balls,target,k,i)
                balls[i][2]=update_y_nocol_(balls,target,k,i)
        
        elif float(target[k])>=min_time[0] and min_time!=-1:
            target[k]=float(target[k])-min_time[0]
            for i in range(len(balls)):
                if (balls[i][0]==min_time[1] or balls[i][0]==min_time[2]):
                    break
            for j in range(len(balls)):
                if i==j:
                    continue
                if (balls[j][0]==min_time[1] or balls[j][0]==min_time[2]):
                    balls[i][1]=update_x_befcol(balls,min_time[0],i)#before collsion distance- the original velocity
                    balls[i][2]=update_y_befcol(balls,min_time[0],i) 
                    balls[j][1]=update_x_befcol(balls,min_time[0],j)#before collsion distance- the original velocity
                    balls[j][2]=update_y_befcol(balls,min_time[0],j) 
                    balls_update_vx=update_vx_col(balls,min_time,i,j)
                    balls_update_vy=update_vy_col(balls,min_time,i,j) 
                    break
                else:
                    continue
            for i in range(len(balls)):
                if (balls[i][0]==min_time[1] or balls[i][0]==min_time[2]):
                    
                    if balls[i][0]==min_time[1]:
                        
#                        balls[i][1]=update_x_befcol(balls,min_time[0],i)#before collsion distance- the original velocity
#                        balls[i][2]=update_y_befcol(balls,min_time[0],i)                         
                        balls[i][3]=balls_update_vx[0]#after collision velocity                            
                        balls[i][4]=balls_update_vy[0]
                    elif balls[i][0]==min_time[2]:
                        
#                        balls[i][1]=update_x_befcol(balls,min_time[0],i)#before collsion distance- the original velocity
#                        balls[i][2]=update_y_befcol(balls,min_time[0],i)
                
                        balls[i][3]=balls_update_vx[1]#after collision velocity
                        balls[i][4]=balls_update_vy[1]                        
                else:
                    balls[i][1]=update_x_nocol(balls,min_time[0],i)#after collision distance -updated velocity
                    balls[i][2]=update_y_nocol(balls,min_time[0],i)
            select_time(k,balls,target)
    return balls

def update_vx_col(balls,min_time,i,j):
#    if (balls[i][0]==min_time[0][0]) or (balls[i][0]==min_time[0][1]):
    delta_x=balls[i][1]-balls[j][1]
    delta_y=balls[i][2]-balls[j][2]
    delta_vx=balls[i][3]-balls[j][3]
    delta_vy=balls[i][4]-balls[j][4]
    dot=(delta_x*delta_vx+delta_y*delta_vy)/100
    vx1=balls[i][3]-dot*delta_x
    vx2=balls[j][3]+dot*delta_x
    return (vx1,vx2)

def update_vy_col(balls,min_time,i,j):
    
   delta_x=balls[i][1]-balls[j][1]
   delta_y=balls[i][2]-balls[j][2]
   delta_vx=balls[i][3]-balls[j][3]
   delta_vy=balls[i][4]-balls[j][4]
   dot=(delta_x*delta_vx+delta_y*delta_vy)/100
   vy1=balls[i][4]-dot*delta_y
   vy2=balls[j][4]+dot*delta_y
   return (vy1,vy2)

def update_x_one(balls,target,k):
    balls_i_x=(float(target[k]))*float(balls[0][3])+float(balls[0][1])
    return balls_i_x

def update_y_one(balls,target,k):
    balls_i_y=(float(target[k]))*float(balls[0][4])+float(balls[0][2])
    return balls_i_y

def update_x_nocol_(balls,target,k,i):
    balls_i_x=(float(target[k]))*balls[i][3]+balls[i][1]
    return balls_i_x

def update_y_nocol_(balls,target,k,i): 
    balls_i_y=(float(target[k]))*balls[i][4]+balls[i][2]
    return balls_i_y

def update_x_nocol(balls,target,i):
    balls_i_x=target*balls[i][3]+balls[i][1]
    return balls_i_x
   
def update_y_nocol(balls,target,i): 
    balls_i_y=target*balls[i][4]+balls[i][2]
    return balls_i_y

def update_x_befcol(balls,target,i):
    balls_i_x=balls[i][3]*target+balls[i][1]
    return balls_i_x

def update_y_befcol(balls,target,i):
    balls_i_y=balls[i][4]*target+balls[i][2]
    return balls_i_y

def update_aftercol_x(balls,target,k,i):
    balls_i_x=(float(target[k]))*balls[i][3]+balls[i][1]
    return balls_i_x

def update_aftercol_y(balls,target,k,i):
    balls_i_y=(float(target[k]))*balls[i][4]+balls[i][2]
    return balls_i_y
       
def main():
    target=[]
    time_list = []
    time_num = []
    time_list = sys.argv[1:]
    for i in time_list:
        try:
            time_num.append(float(i))
        except:
            exit(2)
    for i in time_num:
        if i >= 0:
            target_ori.append(i)
    if len(target_ori) == 0:
        exit(2)
    target_ori.sort()
    target=copy.deepcopy(target_ori)
    
    balls=[]
    ball_list = []
    flag = 0
    rc = 0
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line !='':
            ball_list.append(line.split())
        else:
            if flag==0:
                flag=1
            else:
                rc = 1
                exit(1)
    for k in ball_list:
        if len(k)!=5:
            exit(1)
        else:
            try:
                for j in range(1,len(k)):
                    k[j] = float(k[j])
            except:
                exit(1)
        balls_ori.append(k)
        
    for k in range(len(target_ori)):
        balls=copy.deepcopy(balls_ori)
        select_time(k,balls,target)
        print(target_ori[k])
        for j in range(len(balls)):
            for k in balls[j]:
                print(k,end=' ')
            print('')
#    balls=[]
#    f=open('/Users/wangmengxi/Documents/mercy/wmx_ec602/hw6/random1.coordinates','r') 
#    while 1:
#        line=f.readline()
#        line=line.split()
#        if not line:
#            break;
#        balls_ori.append(line)
#        
#    target=[]
#    for i in range(1,len(sys.argv)):
#        target_ori.append(sys.argv[i])
#    target=copy.deepcopy(target_ori)
#
#    for k in range(len(target_ori)):
#        balls=copy.deepcopy(balls_ori)
#        select_time(k,balls,target)
#        print(target_ori[k])
#        for j in range(len(balls)):
#            for k in balls[j]:
#                print(k),
#            print('')
if __name__ == '__main__':
    main()

#    collision_time()