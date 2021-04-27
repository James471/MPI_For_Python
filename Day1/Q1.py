from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
np.random.seed(10) #Comment and uncomment this line depending whether you want seeding or not
print(np.random.random())