m = int(input())
n = int(input())
square = []

for i in range(101):
    if (i * i) >= m and (i * i) <= n:
        square.append(i * i)

if not square:
    print(-1)
else:
    print(sum(square))
    print(min(square))