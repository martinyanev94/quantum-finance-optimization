import time
import random

# Simulate a list of timestamps
timestamps = [random.randint(1, 10000) for _ in range(1000)]

start_time = time.time()
sorted_timestamps = sorted(timestamps)  # Efficient sorting
end_time = time.time()

print(f"Sorted timestamps in {end_time - start_time:.4f} seconds:")
print(sorted_timestamps)
