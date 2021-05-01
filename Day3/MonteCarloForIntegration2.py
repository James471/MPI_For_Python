from mpi4py import MPI
import numpy as np

def fun(x):
    return x*x

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a, b, n = None, None, None

if rank == 0:
    a = int(input("Enter the lower limit:"))
    b = int(input("Enter the upper limit:"))
    n = int(input("Enter the number of points:"))

a, b, n = comm.bcast(obj=(a,b,n))
localA = a + rank*((b-a)/size)
localB = localA + ((b-a)/size)
localIntegral = 0
totalIntegral = 0

for i in range(1,n):
    x = localA + (localB-localA)*np.random.random()
    localIntegral += fun(x)
localIntegral *= (localB-localA)/n

totalIntegral = comm.reduce(localIntegral, MPI.SUM)
if rank == 0:
    print("Total Integral =", totalIntegral)