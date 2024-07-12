# 1

a = input().split()
lst = [int(num) for num in a]

def inversions(lst):
    len_lst = len(lst)
    inv_count = 0
    for i in range(len_lst):
        for j in range(i+1, len_lst):
            if lst[i] > lst[j]:
                inv_count += 1
    return inv_count

print(inversions(lst))

# 3

n = int(input())
def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n-1) + 1

print(hanoi(n))