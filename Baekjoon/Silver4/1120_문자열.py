a, b = input().split()
result = []

# b 문자열에서 a 문자열 길이만큼의 부분을 순회하면서 차이를 계산
for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        # a와 b의 각 문자를 비교하여 다르면 count 증가
        if a[j] != b[i + j]:
            count += 1
    result.append(count)
    
print(min(result))