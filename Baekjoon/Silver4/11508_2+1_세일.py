n = int(input())
prices = []

for _ in range(n):
    prices.append(int(input()))

prices.sort(reverse=True)

total = 0

# 3개씩 묶어서 3번째로 싼 제품을 선택하고 그 가격을 더함
for i in range(2, len(prices), 3):  # 시작 인덱스는 2, 종료 인덱스는 prices의 길이, 간격은 3
    total += prices[i]

# 전체 가격에서 2+1 세일에 해당하는 제품 가격을 뺌
print(sum(prices) - total)