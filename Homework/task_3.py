# 1

c,sum = 0,0
while True:
    zp = float(input())
    if zp == 0:
        break
    c +=1
    sum += zp
print(sum/c)

# 2

n = input()
digits = {}
for i in n:
    if i not in digits:
        digits[i] = 1
    else:
        digits[i] += 1
for i in sorted(digits):
    print(f"{i} - {digits[i]}")

# 3

max_length = 0
max_key = 0
s = input().split()
for k, v in enumerate(s):
    l = len(v)
    if l > max_length:
        max_length = l
        max_key = k
print(s[max_key])