from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank%2 == 0:
    print("My rank is {} and it's even.".format(rank))
else:
    print("My rank is {} and it's odd.".format(rank))