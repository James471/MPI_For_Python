from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

xi = 0
xf = 1
nTrap = 200
h = (xf-xi)/nTrap

assert nTrap%size == 0, "size must divide nTrap"
localNTrap = int(nTrap/size)

localXi = xi + rank*localNTrap*h
localXf = localXi + localNTrap*h
integ = (localXi*localXi + localXf*localXf)/2

for i in range(1,localNTrap,1):
    localXi += h
    integ += localXi*localXi

integ *= h

if rank!=0:
    comm.send(integ, dest=0, tag=0)
else:
    for j in range(1,size,1):
        integ += comm.recv(source=j, tag=0)
    print("Integral =", integ)