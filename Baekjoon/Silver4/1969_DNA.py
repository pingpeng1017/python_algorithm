n, m = map(int, input().split())
dna_list = []

for _ in range(n):
    dna_list.append(input())

count = 0  # Hamming Distance의 합
result = ''  # 결과 DNA 문자열

# 각 열에 대해 최빈 뉴클레오티드 찾기
for i in range(m):
    dna = [0, 0, 0, 0]  # A, C, G, T
    
    # 해당 열에서 A, C, G, T의 개수 세기
    for j in range(n):
        if dna_list[j][i] == 'A':
            dna[0] += 1
        elif dna_list[j][i] == 'C':
            dna[1] += 1
        elif dna_list[j][i] == 'G':
            dna[2] += 1
        elif dna_list[j][i] == 'T':
            dna[3] += 1
    
    # 최빈 뉴클레오티드의 인덱스 찾기
    idx = dna.index(max(dna))
    
    # 결과 문자열에 추가
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'
    
    # Hamming Distance의 합 계산
    count += n - max(dna)

print(result)
print(count)