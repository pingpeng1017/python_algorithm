s = input()
count = 0

# 문자열을 순회하면서 연속된 숫자 그룹의 변경 감지
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        count += 1  # 다른 문자가 나타날 때마다 횟수 증가

print((count + 1) // 2)