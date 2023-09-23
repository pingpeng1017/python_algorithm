test_case = 0

while True:
    l, p, v = map(int, input().split())
    
    # 입력이 0이면 종료
    if l == 0 and p == 0 and v == 0:
        break
    test_case += 1
    
    # 캠핑장을 최대 며칠동안 사용할 수 있는지 계산
    days = (v // p) * l + min(v % p, l)
    
    print(f"Case {test_case}: {days}")