import time
import timeit

start = time.time()
a = [i for i in range(100000)]
delta = time.time() - start
print(delta)


print(timeit.timeit('a = [i for i in range(100000)]', number=100))
