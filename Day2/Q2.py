from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

xi = 0
xf = np.pi
m = 200     #Number of points to be summed over in each interval
localIntervalSize = (xf-xi)/size       #We divide the range of integration equally among all the processors


localXi = xi + rank*localIntervalSize   #Calculating the interval for each processor using its rank.
localXf = localXi + localIntervalSize
h = (localXf-localXi)/m
integ = (np.cos(localXi) + np.cos(localXf))/3

for i in range(1,m,1):
    localXi += h
    if i%2 == 0:
        integ += 2*np.cos(localXi)
    else :
        integ += 4*np.cos(localXi)

integ *= h

if rank!=0:
    comm.send(integ, dest=0, tag=0)
    print("{} sent by processor {}".format(integ, rank))
else:
    for j in range(1,size,1):
        num = comm.recv(source=j, tag=0)
        print("Received {} from processor {}".format(num, j))
        integ += num
    print("Integral =", integ)