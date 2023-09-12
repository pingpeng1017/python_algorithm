s = input()
arr = [0] * 26

for i in s:
    arr[ord(i) - 97] += 1
print(*arr)  # 배열의 모든 원소를 공백으로 구분하여 출력