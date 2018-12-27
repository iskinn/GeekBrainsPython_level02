import cProfile

def get_len(array):
    return len(array)

def get_sum(array):
    sum_ = 0
    for i in array:
        sum_ += 1
    return sum_

def maim():
    lst = [i for i in range(10000)]
    len = get_len(lst)
    sum = get_sum(lst)
    return sum

#cProfile.run(maim)
print(maim())
