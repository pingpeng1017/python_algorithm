student = int(input())
num = list(map(int, input().split()))
order = []

for i in range(student):
    order.insert(i - num[i], i + 1)

print(*order)