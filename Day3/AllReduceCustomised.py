from mpi4py import MPI
import numpy as np

'''
Something you should know about reduce is that it 
takes 2 objects from 2 processors(one from each) and
calls the op function with them. Then, it takes the 
object returned by the result and takes one object
from another processor and then calls op with this object
and the result object from the last call. This goes on till
it's done with all the objects. The object returned by op in the 
end is returned by reduce.
'''

class Custom:
    def __init__(self, value, rank):
        self.value = value
        self.rank = rank

def minLoc(obj1, obj2):
    if obj1.value<obj2.value:
        return obj1
    return obj2

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

obj = comm.allreduce(Custom(np.random.random(), rank), minLoc)
print("I processor {} know that the minimum value is {} and it was sent by processor {}".format(rank, obj.value, obj.rank))