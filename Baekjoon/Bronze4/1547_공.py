m = int(input())
cups = [1, 2, 3]

for i in range(m):
    x, y = map(int, input().split())
    c1 = cups.index(x)
    c2 = cups.index(y)
    cups[c1], cups[c2] = cups[c2], cups[c1]
     
print(cups[0])