import numpy as np
import matplotlib.pyplot as plt
import statistics 
import pylab

filename=input('Which data set did you use?:')
X=0
with open('S'+filename) as f:
    liste = f.readlines()
    A1=[]
    A2=[]
    A3=[]
    avg=0
    for line in liste:
        line=line.split()
        X=X+1
        A1.append(float(line[1]))
        A2.append(float(line[2]))
        A3.append(float(line[3]))
        #avg=float(line[1])
        
with open('AR'+filename) as f:
    liste = f.readlines()
    B1=[]
    B2=[]
    B3=[]
    avg=0
    for line in liste:
        line=line.split()
        #print(line)
        B1.append(float(line[1]))
        B2.append(float(line[2]))
        B3.append(float(line[3]))
        #avg=float(line[1])
        
with open('NR'+filename) as f:
    liste = f.readlines()
    C1=[]
    C2=[]
    C3=[]
    avg=0
    for line in liste:
        line=line.split()
        #print(line[2])
        C1.append(float(line[1]))
        C2.append(float(line[2]))
        C3.append(float(line[3]))
        #avg=float(line[1])

S=0
count=0
'''for x in C3[0:500000]:
    count+=1
    if x>1000:
        print(x,count)'''

smother=100
print(statistics.mean(A1[S:X]),statistics.mean(B1[S:X]))
D1 = [float(a) / float(b) for a,b in zip(A1[S:X], B1[S:X])]
D1smooth = [0] * X
#print(len(D1))
for i in range(0,X):
    sumS=0.0
    antal=0
    
    for j in range(max(0,i-smother),min(i+smother,X-1)):
        #sumS+=D1[j]
        antal+=1
    D1smooth[i]=sumS/antal
         

plt.figure(0)
plt.title('Smoothed rcatio (our algorithm)/(always recomputing)')
plt.plot(D1smooth)
plt.show()
plt.figure(1)
plt.ylabel('Cost')
#plt.rc('text', usetex=True)

plt.plot(A1[S:X],label = 'Our Alg')
plt.plot(B1[S:X],label = 'MeyersonRec')
plt.plot(C1[S:X],label = 'MeyersonSingle')
pylab.legend(loc='upper left')
print('hej')
plt.xlabel('Number of updates')
plt.show()

plt.figure(2)
plt.ylabel('Clusters opened (log scale)')
plt.semilogy(A2[S:X],label = 'Our Alg')
plt.semilogy(B2[S:X],label = 'MeyersonRec')
plt.semilogy(C2[S:X],label = 'MeyersonSingle')
pylab.legend(loc='upper left')
plt.xlabel('Number of updates')



plt.figure(3)
plt.ylabel('Time in seconds (log scale)')
plt.semilogy(A3[S:X],label = 'Our Alg')
plt.semilogy(B3[S:X],label = 'MeyersonRec')
plt.semilogy(C3[S:X],label = 'MeyersonSingle')
pylab.legend(loc='upper left')
plt.xlabel('Number of updates')

