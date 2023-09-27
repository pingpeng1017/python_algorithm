num = int(input())

# 도화지를 나타내는 2차원 리스트
paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(num):
    x, y = map(int, input().split())
    
    # 색종이가 덮는 영역을 1로 표시
    for i in range(x, x + 10):  # 가로 길이
        for j in range(y, y + 10):  # 세로 길이
            paper[i][j] = 1

result = 0

for row in paper:
    # 각 행에서 1의 개수를 세어 result에 더하기
    result += row.count(1)
print(result)