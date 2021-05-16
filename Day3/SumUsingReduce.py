from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

rand = np.random.random()
print("Processor {} generated random number {}".format(rank, rand))
sum = comm.reduce(rand, MPI.SUM)    #Finds the sum of the random numbers
if rank == 0:
    print(sum)