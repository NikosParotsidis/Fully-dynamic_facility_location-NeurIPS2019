import random
import math
import numpy as np
import time

#calculates minimum distance from a node to a set of nodes
def closest_node_dist(node, nodes):
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    return math.sqrt(min(dist_2))

#If we want to calculate the sum of the actual distances to closest center and not just the assigned one
def actualcost(data, facilities):
    sum1=0.0
    for x in data:
        sum1+=closest_node_dist(x,facilities)
    return sum1

def meyerson(data, dimension, f,list1):
    facilities= []
    cost=0
    counter=0
    numberofcenters=0
    for point in data:
        counter=counter+1
        if numberofcenters>0:
            nearest = closest_node_dist(point,facilities)
        else:
            nearest = f+1
        if random.uniform(0,1)*f<nearest:
            facilities.append(point)
            cost=cost+f
            numberofcenters+=1
        else:
            cost=cost+nearest
        list1[counter-1]=numberofcenters
    #activate below if you want actual cost and not assigned cost"
    #cost=actualcost(data,facilities)+f*numberofcenters
    return facilities,cost,numberofcenters

def meyersonmanytimes(data, dimension, f, times):
    minimum=meyerson(data,dimension,f)
    for i in range(1,times):
        run=meyerson(data,dimension,f)
        if run[1]<minimum[1]:
            minimum=run
    return minimum


def DFL(data,dimension,f,n,window,filename):
    filename='NR'+filename
    g = open(filename,'w+')
    currentcost=0
    totalfacil=0
    start = time.time()
    currentdata=data[0:window]
    currentdata= np.random.permutation(currentdata)
    numberoffacilwhenadded=[0]*window
    currentfacil, currentcost, numberoffacil=meyerson(currentdata,dimension,f,numberoffacilwhenadded)
    totalfacil+=numberoffacil
    g.write(str(0)+ " "+str(currentcost)+ " " + str(totalfacil) + " "+  str(time.time()-start)+ '\n')
    for i in range(1,n-window):
        currentdata=data[i:i+window]
        #print(currentcost, costReMey)
        mod = (i-1)%window
        currentcost-=closest_node_dist(data[i-1],currentfacil[0:numberoffacilwhenadded[mod]])
        nearest=closest_node_dist(data[i+window-1],currentfacil)
        if nearest<f*random.uniform(0,1):
            currentcost=currentcost+nearest
        else:
            currentcost=currentcost+f
            totalfacil+=1
            currentfacil.append(data[i+window-1])
        numberoffacilwhenadded[i%window]=totalfacil
        if i%(n/10)==0:
            print(i,totalfacil,currentcost, time.time()-start)
        g.write(str(i)+ " "+str(currentcost)+ " " + str(totalfacil) + " "+  str(time.time()-start)+ '\n')

        
   
        