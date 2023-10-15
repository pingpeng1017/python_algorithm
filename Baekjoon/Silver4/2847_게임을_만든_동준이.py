n = int(input())
score = [int(input()) for _ in range(n)]
count = 0

# 뒤에서부터 역순으로 레벨 확인
for i in range(n - 1, 0, -1):
    # 현재 레벨의 점수가 이전 레벨보다 작거나 같으면
    if score[i] <= score[i - 1]:
        # 감소시켜야 하는 횟수 누적
        count += score[i - 1] - score[i] + 1
        # 현재 레벨을 이전 레벨보다 1 작게 만듦
        score[i - 1] = score[i] - 1

print(count)