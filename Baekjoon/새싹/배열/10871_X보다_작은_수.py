N, X = map(int, input().split())
A = list(map(int, input().split()))

for num in range(N):
    if A[num] < X:
        print(A[num], end = " ")