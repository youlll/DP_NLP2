#coding=utf-8
import random
import numpy as np
s1 = 0.2
s2 = 0.6
p = 0.4
q = 0.6
r = 0.6
n = 1000
s1lst = [0 for i in range(n)]
s2lst = [0 for i in range(n)]
s3lst = [0 for i in range(n)]
def toss(s1, s2, p, q, r, n):
    s3 = 1-s1-s2
    tlist = [0 for i in range(n)]
    #x=s1,s2,s3 y=p,q,r n>=1
    for i in range(n):
        if random.random()<(s1*p+s2*q+s3*r):
            tlist[i]=1
    return tlist

#def myEM(tlist):

tlist = toss(s1, s2, p, q, r, n)
s1e = 0.3
s2e = 0.5
pe = 0.3
qe = 0.6
re = 0.65
while True:
    #step E
    for i in range(n):
        s1lst[i] = ( s1e*(pe**tlist[i])*((1-pe)**(1-tlist[i])) ) /\
        ( s1e*(pe**tlist[i])*((1-pe)**(1-tlist[i])) + s2e*(qe**tlist[i])*((1-qe)**(1-tlist[i])) + \
          (1-s1e-s2e)*(re**tlist[i])*((1-re)**(1-tlist[i])) )
        s2lst[i] = ( s2e*(qe**tlist[i])*((1-qe)**(1-tlist[i])) ) /\
        ( s1e*(pe**tlist[i])*((1-pe)**(1-tlist[i])) + s2e*(qe**tlist[i])*((1-qe)**(1-tlist[i])) + \
          (1-s1e-s2e)*(re**tlist[i])*((1-re)**(1-tlist[i])) )
        s3lst[i] = 1-s1lst[i]-s2lst[i]
    '''
    for i in range(n):
        s1lst[i] = ( s1e*(pe**tlist[i])*((1-pe)**(1-tlist[i])) ) /\
        ( s1e*(pe**tlist[i])*((1-pe)**(1-tlist[i])) + s2e*(qe**tlist[i])*((1-qe)**(1-tlist[i]))) 
        s2lst[i] = ( s2e*(qe**tlist[i])*((1-qe)**(1-tlist[i])) ) /\
        ( s1e*(pe**tlist[i])*((1-pe)**(1-tlist[i])) + s2e*(qe**tlist[i])*((1-qe)**(1-tlist[i])) )
        s3lst[i] = 1-s1lst[i]-s2lst[i]
    '''
    #step M
    s1elast = s1e
    s2elast = s2e
    pelast = pe
    qelast = qe
    relast = re
    s1e = np.mean(s1lst)
    s2e = np.mean(s2lst)
    num1 = [x*y for x,y in zip(s1lst,tlist)]
    num2 = [x*y for x,y in zip(s2lst,tlist)]
    num3 = [x*y for x,y in zip(s3lst,tlist)]
    pe = np.sum(num1)/np.sum(s1lst)
    qe = np.sum(num2)/np.sum(s2lst)
    re = np.sum(num3)/np.sum(s3lst)
    if np.sum( abs(s1e-s1elast)+ abs(s2elast - s2e)+abs(pelast - pe)+abs(qelast - qe)+abs(relast - re) )<0.001:
        break
print('s1=',s1e,'\ns2=',s2e,'\np=',pe,'\nq=',qe,'\nr=',re)
print('m=', np.sum(tlist)/n)
print('me=',s1e*pe+s2e*qe+(1-s1e-s2e)*re)