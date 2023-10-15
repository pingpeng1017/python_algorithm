n = int(input())

# 5키로 봉지로 최대한 채우기
bag5 = n // 5

# 나머지를 3키로 봉지로 채울 수 있는지 확인
while bag5 >= 0:
    rest = n - bag5 * 5
    
    # 나머지가 3의 배수인 경우
    if rest % 3 == 0:
        bag3 = rest // 3
        print(bag5 + bag3)
        break
    else:
        # 5키로 봉지를 줄이고 다시 시도
        bag5 -= 1
else:
    print(-1)