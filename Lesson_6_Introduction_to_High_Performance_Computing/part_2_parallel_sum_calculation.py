from multiprocessing import Pool
import numpy as np

def calculate_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    # Generate an array of numbers
    large_array = np.random.rand(1_000_000).tolist()
    
    # Define the number of processes
    num_processes = 4
    
    # Create a pool of workers
    with Pool(num_processes) as pool:
        # Split the array into chunks for each process
        chunk_size = len(large_array) // num_processes
        chunks = [large_array[i:i + chunk_size] for i in range(0, len(large_array), chunk_size)]
        
        # Calculate sums in parallel
        results = pool.map(calculate_sum, chunks)
    
    # Combine results
    total_sum = sum(results)
    print(f"The total sum is {total_sum}")
