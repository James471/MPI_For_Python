from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank!=0:
    comm.send(rank, 0, tag=0)
    print("Sent {} to processor {}".format(rank,0))
else:
    sum = rank
    for i in range(1,size,1):
        num = comm.recv(source = i, tag=0)
        print("{} received from processor {}".format(num,i))
        sum += num
    print(sum)