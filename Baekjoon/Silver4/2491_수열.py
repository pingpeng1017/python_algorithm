n = int(input())
num = list(map(int, input().split()))

# 증가하는 부분 수열 길이를 저장하는 DP 테이블
dp1 = [1] * n
# 감소하는 부분 수열 길이를 저장하는 DP 테이블
dp2 = [1] * n

for i in range(n - 1):
    if num[i + 1] >= num[i]:
        dp1[i + 1] += dp1[i]
        
for i in range(n - 1):
    if num[i + 1] <= num[i]:
        dp2[i + 1] += dp2[i]
    
print(max(max(dp1), max(dp2)))