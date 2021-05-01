from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

rand = np.random.random()
print("Hi, from processor {}. Random number generated = {}".format(rank, rand))
mx = None
loc = None
mx, loc = comm.allreduce((rand,rank), MPI.MAXLOC)
print("I processor {} know that the maximum value is {} and it was generated by processor {}".format(rank, mx, loc))