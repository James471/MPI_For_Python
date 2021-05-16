from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank!=0:
    comm.send(rank, 0, tag=0)   #Each processor except processor 0 sends it's rank to processor 0. You can send any object you want by passing it as data parameter. The tag is meant to identify the data.
    print("Sent {} to processor {}".format(rank,0))
else:
    sum = rank
    for i in range(1,size,1):
        num = comm.recv(source = i, tag=0)  #Processor 0 receives the data with tag=0 from each processor. source is the processor rank of the processor sending the data.
        print("{} received from processor {}".format(num,i))
        sum += num
    print(sum)