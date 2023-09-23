height = [int(input()) for i in range(9)]
total = sum(height)
a = 0
b = 0

# 두 명을 선택하여 제외할 때의 경우
for i in range(9):
    for j in range(i + 1, 9):
        if total - (height[i] + height[j]) == 100:
            a = height[i]
            b = height[j]
            
height.remove(a)
height.remove(b)
height.sort()

for i in height:
    print(i)