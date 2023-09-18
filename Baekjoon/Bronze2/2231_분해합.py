n = int(input())

for i in range(n):
    temp = sum(map(int, str(i)))
    result = temp + i
    if result == n:
        print(i)
        break
else:
    print(0)