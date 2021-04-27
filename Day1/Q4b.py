import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

arr = [i for i in range(0,12)]
arr = np.array(arr).reshape((6,2))

print("The following output was sent by processor ranked", rank)
for i in range(rank,6,2):
    print(arr[i][0], arr[i][1])