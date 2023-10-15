from itertools import permutations

n = int(input())
k = int(input())
num = []

for _ in range(n):
    num.append(input())

# 중복 제거  
result = set()

# 가능한 모든 순열 생성
for i in permutations(num, k):
    result.add(''.join(i))  # 튜플의 각 원소들을 문자열로 합치기

print(len(result))