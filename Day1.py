#Never use import *
#There is a name class with Exception class in mpi4py and python
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print("Hello world from rank", str(rank), "of", str(size))