n = int(input())
file_names = [input() for _ in range(n)]

# 첫번째 파일 이름을 패턴으로 초기화
pattern = list(file_names[0])

# 나머지 파일들과 비교
for i in range(1, n):
    for j in range(len(pattern)):
        if file_names[i][j] != pattern[j]:
            pattern[j] = '?'

print(''.join(pattern))  