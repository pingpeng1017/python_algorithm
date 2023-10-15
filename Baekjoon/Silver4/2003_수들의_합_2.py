n, m = map(int, input().split())
a = list(map(int, input().split()))
count = 0

# 시작점을 기준으로 가능한 모든 구간을 탐색
for start in range(n):
    sum = 0
    
    # 시작점부터 끝까지 누적 합 계산
    for end in range(start, n):
        sum += a[end]
        
        # 누적 합이 목표값과 일치하는 경우
        if sum == m:
            count += 1
            break
        
        # 누적 합이 목표값보다 큰 경우
        elif sum > m:
            break
    
print(count)   