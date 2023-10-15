from collections import deque

n = int(input())
d = deque(range(1, n + 1))

while len(d) > 1:
    # 맨 위의 카드를 버리기
    d.popleft()
    
    # 그 다음 카드를 맨 아래로 옮기기
    d.append(d.popleft())

print(d[0])