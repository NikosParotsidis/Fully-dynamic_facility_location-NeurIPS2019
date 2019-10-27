import MeyersonN as MN
import MeyersonR as MR
import MeyersonS as MS
import numpy as np
import math


file=input('Enter datafile name: ')
openingcost= float(input('Enter f value: '))
numberofiterations=int(input('Enter number of iterations: '))
windowsize=int(input('Enter window size: '))
startvariable=int(input('Input first number variable: '))
endvariable=int(input('Input last number variable: '))

print('you are using data set: '+file)
print('with f value: ', openingcost)
print('Will run for this many iterations: ',numberofiterations)
print('with this window size: ', windowsize)

with open(file) as f:
    liste = f.readlines()
    newlist = []
    countlines=0
    for line in liste:
        line = line.replace(',',' ')
        line= line.split()
        line=line[startvariable:endvariable]
        line = list((map(float,line)))
        newlist.append(line)
        countlines+=1
    dimension=len(newlist[1])

    print('Dimension of your data:',dimension)
    listofzeros = [0]*dimension
    newlist=newlist[:numberofiterations]
    for x in newlist:
        for i in range(0,dimension):
            listofzeros[i]+=x[i]
    averages = [0]*dimension
    for i in range(0,dimension):
        averages[i]=listofzeros[i]/countlines
    variances = [0]*dimension
    for x in newlist:
        for i in range(0,dimension):
            variances[i]+=(x[i]-averages[i])**2

    for i in range(0,dimension):
        variances[i]=math.sqrt(variances[i])
    
    for x in newlist:
        for i in range(0,dimension):
            x[i]=(x[i]-averages[i])/variances[i]
    print('first two rows:',newlist[0:2])    
    #print(newlist)    
    array = np.asarray(newlist)
    
    #print(array[0:10])
    
    #print(array)
    print('starting never recomputing algorithm')
    MN.DFL(array,dimension,openingcost,numberofiterations,windowsize,file)
    print('starting always recomputing algorithm')
    MR.DFL(array,dimension,openingcost,numberofiterations,windowsize,file)
    print('starting our algorithm')
    MS.DFL(array,dimension,openingcost,numberofiterations,5,windowsize,file)



