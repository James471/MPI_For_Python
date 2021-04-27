#Never use import *
#There is a name class with Exception class in mpi4py and python
from mpi4py import MPI

#We don't need to initialize and terminate unlike the C++ Implementation
comm = MPI.COMM_WORLD #Returns an object containing all the information passed to the processor while running the script. 
size = comm.Get_size() #Gives the total number of processors being used
rank = comm.Get_rank() #The procid equivalent of the C++ Implementation

print("Hello world from rank", str(rank), "of", str(size))