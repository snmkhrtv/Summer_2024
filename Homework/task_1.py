x = float(input())
y = float(input())


# 1
print(x+y, x*y)


# 2
print(max(x+y, x-y, x*y, x/y, x//y))


# 3
a=0
b=0
if x+y>x-y:
    a=x+y
if x*y>x/y:
    b=x*y
c =  x//y
if a>b>c:
    mid=b
elif c>b>a:
    mid=b
elif a>c>b:
    mid=c
elif c>a>b:
    mid=a
elif b>a>c:
    mid=a
elif b>c>a:
    mid=c

print(mid)