import time

start = time.perf_counter()

for i in range(10_000_000):
    x = i * i

end = time.perf_counter()

print(f"Execution time: {end - start:.4f} seconds")