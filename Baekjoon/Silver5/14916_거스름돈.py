n = int(input())
count = 0

# 5원짜리 동전을 최대한 사용하여 거슬러주기
while n > 0:
    if n % 5 == 0:
        count += n // 5
        break
    n -= 2
    count += 1

if n < 0:
    print(-1)
else:
    print(count)