import random
from random import shuffle
import timeit
import pandas as pd
import numpy as np
import pylab as py

#randomsort vs bubblesort
############################
def randomsort(n): #n should be greater than 2. I did 10 for a test.
    nums=range(1,100)
    computime=[]

    for i in range(2,n):
        l=random.sample(nums,i)
        start = timeit.default_timer()
        while all(l[j] < l[j+1] for j in xrange(len(l)-1)) ==False:
            l = sorted(l, key=lambda k: random.random())
        stop = timeit.default_timer()
        com_time = stop - start
        
        computime.append(com_time)
    return computime
randomsort(10)

d=[]
for i in range(1,11): #this is to calculate average time
    out=randomsort(10)
    d.append(out)
len(d)
len(d[0])
simlist = pd.DataFrame(
    {2: d[0],
     3: d[1],
     4: d[2],
     5: d[3],
     6: d[4],
     7: d[5],
     8: d[6],
     9: d[7],
     10: d[8],
     11: d[9],
    })
final=np.transpose(simlist)

b=[]
for i in range(8):
    a=final[i].mean()
    b.append(a)

#############################################

def bubblesort(n): #n should be greater than 2. I did 10 for a test.
    nums=range(1,100)
    computime=[]
    #size=[]
    for i in range(2,n):
        l=random.sample(nums,i)
        start = timeit.default_timer()
        changed=True
        while changed:
             changed = False
             for j in range(len(l) - 1):
                 if l[j] > l[j+1]:
                     l[j], l[j+1] = l[j+1], l[j]
                     changed = True
                 stop = timeit.default_timer()
             com_time = stop - start
        computime.append(com_time)
    return computime
df=bubblesort(10)
len(df)

d=[]
for i in range(1,11): #this is to calculate average time
    out=bubblesort(10)
    d.append(out)
len(d)
len(d[0])
simlist = pd.DataFrame(
    {2: d[0],
     3: d[1],
     4: d[2],
     5: d[3],
     6: d[4],
     7: d[5],
     8: d[6],
     9: d[7],
     10: d[8],
     11: d[9],
    })
final=np.transpose(simlist)


s=[]
for i in range(8):
    a=final[i].mean()
    s.append(a)
###########################

py.plot(range(2,10), s, label = 'Bubble Sort')
py.xlabel('Size of Sample')
py.ylabel('Average Time')
py.title("Computing time and sorting algorithm: Bubble sort only")
py.legend()
  

py.savefig('graph_only_bubble.png') 
#bubble only. I need to show this becuase in a comparison graph, the increase of computation time is not clear.




py.plot(range(2,10), b, label = 'Random Sort')
py.xlabel('Size of Sample')
py.ylabel('Average Time')
py.title("Computing time and sorting algorithm")
py.legend()#
  

py.savefig('graph_compare.png') 
#it looks like bubble doesn't increase by size of sample, but it is only because random sorting computing time is exponentially increasing
