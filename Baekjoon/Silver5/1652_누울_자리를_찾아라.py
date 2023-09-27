n = int(input())
room = [input() for _ in range(n)]

garo = 0
sero = 0

# 가로로 누울 수 있는 자리 검사
for row in room:
    count = 0
    for cell in row:
        if cell == '.':
            count += 1
        else:
            if count >= 2:
                garo += 1
            count = 0
    if count >= 2:
        garo += 1

# 세로로 누울 수 있는 자리 검사
for col in range(n):
    count = 0
    for row in range(n):
        if room[row][col] == '.':
            count += 1
        else:
            if count >= 2:
                sero += 1
            count = 0
    if count >= 2:
        sero += 1

print(garo, sero)