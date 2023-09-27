x = int(input())
line = 1

# x가 현재 대각선 번호보다 큰 동안 반복
while x > line:
    x -= line
    line += 1

# 대각선 번호가 짝수인 경우
if line % 2 == 0:
    print(f'{x}/{line - x + 1}')
    
# 홀수인 경우
else:
    print(f'{line - x + 1}/{x}')