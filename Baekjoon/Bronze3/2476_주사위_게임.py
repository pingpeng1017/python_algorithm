n = int(input())
list = []

for i in range(n):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        money = 10000 + a * 1000
    elif a == b:
        money = 1000 + a * 100
    elif a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = max(a, b, c) * 100
    list.append(money)

print(max(list))