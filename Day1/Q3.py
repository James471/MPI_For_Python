#I hope there are better ways to do this but this is Day1
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    s = 0
    for i in range(1,10):
        s += i
    print("Sum =", s)
elif rank == 1:
    p = 1
    for i in range(1,10):
        p *= i
    print("Product =", p)
else:
    s = 0
    for i in range(1,10):
        s += i*i
    print("Sum of square =", s)
