from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

rand = np.random.random()
print("Hi, from processor {} with value {}".format(rank, rand))
max = comm.allreduce(rand, MPI.MAX)
print("I, processor {} know that the maximum value is {}".format(rank, max))
