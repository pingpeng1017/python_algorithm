n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
    
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    
    sum = 0
    for row in range(i - 1, x):
        for col in range(j - 1, y):
            sum += arr[row][col]
    print(sum)