#1
lst = input().split(' ')

def ind(lst):
    min_val, max_val = min(lst), max(lst)
    min_ind = [i for i, x in enumerate(lst) if x == min_val]
    max_ind = [i for i, x in enumerate(lst) if x == max_val]
    return min_ind, max_ind

min_ind, max_ind = ind(lst)
print(min_ind, max_ind)

#2
import itertools

a = [print(item) for i in range(10) for item in itertools.repeat(i,i) if i<10]

#3
str = input()

def numbers(str):
    lst = str.split(',')
    result = []
    for n in lst:
        start, end = map(int, n.split('-'))
        result.extend(range(start, end + 1))
    return result

print(numbers(str))
