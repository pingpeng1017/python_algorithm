num = list(map(int, input().split()))
n = 1

while True:
    count = 0
    for i in num:
        if n % i == 0:
            count += 1
            
    if count >= 3:
        print(n)
        break
    n += 1