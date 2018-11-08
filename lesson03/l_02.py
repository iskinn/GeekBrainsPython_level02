from array import array

numbers = array('i',[2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4,  6, 78])
numbers_index = array('i')

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers_index.append(i)

print(' '.join(map(str, numbers_index)))
