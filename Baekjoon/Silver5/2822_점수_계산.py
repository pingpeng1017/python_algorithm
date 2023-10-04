score_list = []
total = 0
num = []  # 상위 5개 문제의 번호를 저장할 리스트

for i in range(1, 9):
    score = int(input())
    score_list.append((i, score))

# 점수를 기준으로 내림차순 정렬
score_list.sort(key=lambda x: x[1], reverse=True)

for j in range(5):
    total += score_list[j][1]
    num.append(score_list[j][0])

print(total)
print(*sorted(num))