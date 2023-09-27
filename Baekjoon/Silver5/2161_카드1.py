from collections import deque

n = int(input())
cards = deque(range(1, n + 1))  # 1부터 N까지의 카드를 큐에 넣음
bin = []

while len(cards) > 1:
    bin.append(cards.popleft())  # 제일 위에 있는 카드를 버림
    cards.append(cards.popleft())  # 제일 위에 있는 카드를 제일 아래로 옮김
    
bin.append(cards[0])  # 마지막 남은 카드를 버린 카드 리스트에 추가

print(*bin)