n = int(input())
m = int(input())
num = list(map(int, input().split()))

count = 0
start, end = 0, n - 1

num.sort()

while start < end:
    sum = num[start] + num[end]
    
    if sum == m:
        count += 1
        start += 1
        end -= 1
    elif sum > m:
        end -=1
    else:
        start += 1

print(count)