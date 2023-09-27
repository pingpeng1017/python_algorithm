arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4):
    left_x, left_y, right_x, right_y = map(int, input().split())
    
    for i in range(left_x, right_x):
        for j in range(left_y, right_y):
            arr[i][j] = 1
            
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1

print(count)