import sys

switch = int(sys.stdin.readline())
status = list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())

for _ in range(students):
    gender, num = map(int, sys.stdin.readline().split())
    
    if gender == 1:
        for i in range(num - 1, switch, num):
            if status[i]:
                status[i] = 0
            else:
                status[i] = 1
    
    else:
        num -= 1  # 인덱스로 사용하기 위해 1 빼기
        left, right = num, num
        
        while left >= 0 and right < switch:
            if status[left] == status[right]:
                if status[left]:
                    status[left] = 0
                    status[right] = 0
                else:
                    status[left] = 1
                    status[right] = 1
            else:
                break
            left -= 1
            right += 1

for i in range(switch):
    print(status[i], end = " ")
    if (i + 1) % 20 == 0:
        print()