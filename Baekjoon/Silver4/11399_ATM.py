n = int(input())
time = list(map(int, input().split()))
total = []

time.sort()

waiting = 0

for i in time:
    waiting += i
    total.append(waiting)

print(sum(total))