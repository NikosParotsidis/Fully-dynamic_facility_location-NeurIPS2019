import random
import math
import numpy as np
import time

def dist(x,y,dimension):
    distance=0
    x=x.split()
    y=y.split()
    for i in range(0,dimension):
        xtal=float(x[i])
        ytal=float(y[i])
        distance+=distance+(xtal-ytal)**2
    return math.sqrt(distance)

def closest_node_dist(node, nodes):
    #print(node, nodes)
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    #print(dist_2)
    return math.sqrt(min(dist_2))

#If we want to calculate the sum of the actual distances to closest center and not just the assigned one
def actualcost(data, facilities):
    sum1=0.0
    for x in data:
        sum1+=closest_node_dist(x,facilities)
    return sum1


def isin(list1,x):
    for y in list1:
        if np.array_equal(x,y):
            return True
    return False 

def meyerson(data, dimension, f,facil,overcount):
    data= np.random.permutation(data)
    #print(data[0:10])
    #setfacil = set(facil)
    #print('agurk')
    #print(setfacil)
    #print(type(setfacil))
    facilities= []
    cost=0
    counter=0
    numberofcenters=0
    for point in data:
        #print(point)
        counter=counter+1
        #if counter % 100==0:
            #print(counter)
        #find nearest facility
        if numberofcenters>0:
            nearest = closest_node_dist(point,facilities)
            #print(nearest)
        else:
            nearest = f+1
            #print('hej')
        if random.uniform(0,1)*f<nearest:
            #open center at this point
            #print('agurk')
            #facilities = np.append(facilities, point)
            facilities.append(point)
            cost=cost+f
            if isin(facil,point):
                #print('already a facil')
                overcount+=1
                #print(overcount)
            else:
                numberofcenters+=1
            
        else:
            cost=cost+nearest
    #print(counter)
    #cost=actualcost(data,facilities)+f*numberofcenters
    return facilities,cost,numberofcenters,overcount

def meyersonmanytimes(data, dimension, f, times):
    minimum=meyerson(data,dimension,f)
    for i in range(1,times):
        run=meyerson(data,dimension,f)
        if run[1]<minimum[1]:
            minimum=run
    return minimum


def DFL(data,dimension,f,n,window,filename):
    filename='AR'+filename
    g = open(filename,'w+')
    costReMey=0
    totalfacil=0
    start = time.time()
    facil=[]
    overcount=0
    for i in range(0,n-window):
        currentdata=data[i:i+window]
        facil, costReMey, numberoffacil,overcount=meyerson(currentdata,dimension,f,facil,overcount)
        totalfacil+=numberoffacil
        #print(currentcost, costReMey)
        if i%100==0:
            print(i,totalfacil,numberoffacil*f/costReMey,costReMey, time.time()-start,overcount)
        g.write(str(i)+ " "+str(costReMey)+ " " + str(totalfacil) + " "+  str(time.time()-start)+ '\n')

        
   

        