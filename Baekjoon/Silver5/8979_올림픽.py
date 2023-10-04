n, k = map(int, input().split())
medals = []

for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    medals.append([gold, silver, bronze, country])

medals.sort(reverse=True)

# 국가 K의 정보 찾기
for i in range(n):
    if medals[i][3] == k:
        index = i
        break

# 국가 k와 메달 수가 동일한 다른 국가 찾기
for j in range(n):
    if medals[index][:3] == medals[j][:3]:
        print(j + 1)
        break