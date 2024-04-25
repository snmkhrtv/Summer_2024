# 1

n = int(input())
for i in range(1,10):
    print(f"{n} x {i} = {n*i}")


# 2

lst = [77, 46, 43, 67]
m = lst[0]
for i in range(len(lst)):
    if m > lst[i]:
        m = lst[i]
print(m)


# 3

n = int(input())
f = 1
for i in range(1,n+1):
    f *= i
print(f)
