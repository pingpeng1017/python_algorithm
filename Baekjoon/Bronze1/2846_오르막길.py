n = int(input())
num = list(map(int, input().split()))
start = 0
max_list = []

for i in range(n - 1):
    if num[i] < num[i + 1]:
        start += num[i + 1] - num[i]
    else:
        max_list.append(start)
        start = 0
max_list.append(start)

print(max(max_list))