#coding=utf-8
import math

from leapfrogreturn import leapfrog

import sys
args=sys.argv
if(len(args)!=7):
    print('Error!')
    exit()

v0=float(args[1])
thetadeg=float(args[2])
theta=thetadeg/360*2*3.14
g=float(args[3])
m=float(args[4])
k=float(args[5])
rate=float(args[6])

ret=leapfrog(v0,thetadeg,g,m,k,rate,True)

print('t:',ret['t'])
print('x:',ret['x'])

