from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

xi = 0
xf = np.pi
nTrap = 200
h = (xf-xi)/nTrap

assert nTrap%size == 0, "size must divide nTrap"
localNTrap = int(nTrap/size)

localXi = xi + rank*localNTrap*h
localXf = localXi + localNTrap*h
integ = (np.cos(localXi) + np.cos(localXf))/3

for i in range(1,localNTrap,1):
    localXi += h
    if i%2 == 0:
        integ += 2*np.cos(localXi)
    else :
        integ += 4*np.cos(localXi)

integ *= h

if rank!=0:
    comm.send(integ, dest=0, tag=0)
else:
    for j in range(1,size,1):
        integ += comm.recv(source=j, tag=0)
    print("Integral =", integ)