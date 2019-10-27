# dynamic-facility-location

Use main file to run all 3 algorithms
You will be asked for the following input
Datafile: your data file either as a csv or space seperated.
opening cost: cost of opening a center
Number of iterations: the number of points you want to use for the experiment, should be lower than the number of points in your data set and larger than the window size
Window size: the size of your window for the experiment
start variable: the first number variable you want to use. 
end variable: the last number variable you want to use.

There will be created 3 output files
AR+datafile which is the data for the always recompute algorithm (number iterations , current cost, total recourse, total time)
NR+datafile which is the date for the never recompute algorithm (number iterations , current cost, total recourse, total time)
S+datafile which is the data for our algorithm (number iterations , current cost, total recourse, total time)

All files space seperated

Cost is the sum of open centers plus the of the distances for each point to the center they are assigned to.

