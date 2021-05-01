from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 1000000
localNInsideCircle = 0
totalNInsideCircle = 0
localN = int(n/size)
for i in range(0, localN):
    x = np.random.random()
    y = np.random.random()
    if(x*x + y*y < 1):
        localNInsideCircle += 1
totalNInsideCircle = comm.reduce(localNInsideCircle, MPI.SUM)
if(rank == 0):
    pi = 4*totalNInsideCircle/n
    print(pi)