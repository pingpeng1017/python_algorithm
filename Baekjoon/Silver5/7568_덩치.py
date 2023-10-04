n = int(input())
people = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append([x, y])
    
rank = [1] * n

for i in range(n):
    for j in range(n):
        if i == j:  # 자기 자신과 비교하는 경우 제외
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end=" ")