from mpi4py import MPI
import numpy as np

def fun(x):
    return x*x

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
a, b, n = None, None, None
localSum = 0
integral = 0
totalSum = 0

if rank == 0:
    a = int(input("Enter lower limit:"))
    b = int(input("Enter upper limit:"))
    n = int(input("Enter the number of points:"))

a, b, n = comm.bcast(obj=(a,b,n))

localN = int(n/size)
for i in range(0,localN):
    x = a + (b-a)*np.random.random()
    localSum += fun(x)
totalSum = comm.reduce(localSum, MPI.SUM, 0)
if rank == 0:
    integral = totalSum*(b-a)/n
    print("Integral =", integral)