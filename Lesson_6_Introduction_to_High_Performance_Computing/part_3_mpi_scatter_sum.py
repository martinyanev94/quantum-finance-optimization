from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initialize data
if rank == 0:
    data = np.random.rand(1000)
else:
    data = None

# Scatter data to all processes
data = comm.scatter(data, root=0)

# Each process computes its local sum
local_sum = np.sum(data)

# Gather all local sums at the root process
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"The total sum is {total_sum}")
