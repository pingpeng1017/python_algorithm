n = int(input())
count = 0
sum = 0
left, right = 1, 1

while left <= n:
    # 현재 합이 목표 값 N보다 작으면 오른쪽 포인터를 이동하여 합을 늘림
    if sum < n:
        sum += right
        right += 1
    # 현재 합이 목표 값 N과 같으면 가지수를 증가하고 왼쪽 포인터를 이동하여 합을 줄임   
    elif sum == n:
        count += 1
        sum -= left
        left += 1
    # 현재 합이 목표 값 N보다 크면 왼쪽 포인터를 이동하여 합을 줄임    
    else:
        sum -= left
        left += 1

print(count)