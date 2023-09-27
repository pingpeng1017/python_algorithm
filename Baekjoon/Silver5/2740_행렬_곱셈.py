# 행렬 A의 크기 N과 M
n, m = map(int, input().split())

# 행렬 A
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
    
# 행렬 B의 크기 M과 K
m, k = map(int, input().split())

# 행렬 B
b =[]
for _ in range(m):
    b.append(list(map(int, input().split())))

# 결과 행렬 C 초기화
c = [[0] * k for _ in range(n)]

# 행렬 곱셈 계산
for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j] += a[i][l] * b[l][j]

for i in c:
    print(*i)