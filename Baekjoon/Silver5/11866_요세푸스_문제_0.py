n, k = map(int, input().split())

circle = list(range(1, n + 1))
result = []

# 제거할 사람의 인덱스를 계산하고 해당 사람을 결과에 추가
idx = 0
for _ in range(n):
    idx = (idx + k - 1) % len(circle)  # 리스트의 범위를 벗어나면 다시 처음부터 시작
    result.append(str(circle.pop(idx)))

print('<' + ', '.join(result) + '>')