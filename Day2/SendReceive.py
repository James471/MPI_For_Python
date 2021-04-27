from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#Here's some trouble. If there is an exception before comm.send(), process 1 will wait for the finishing of process 2 while 
#process 2 will wait for process 1 to send the data. This will send MPI environment into a deadlock state.
#So, it's best to raise an exception and use mpiexec -n 2 python3 -m mpi4py script.py
#This fixes the problem by killing processes.
#It's actually best to do so for all scripts which involve communication.

if size%2 != 0:
    raise("Number of processors must be even")

if rank%2 == 0:
    comm.send(rank, dest=rank+1, tag=0)
    print("Sent {} to processor ranked {}".format(rank, rank+1))
else:
    data = comm.recv(source=rank-1, tag=0)
    print("{} recieved by processor ranked {}".format(data, rank))