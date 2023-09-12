import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = math.ceil(a / c)
f = math.ceil(b / d)
g = max(e, f)

print(l - g)