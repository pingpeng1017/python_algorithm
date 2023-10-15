import math

t = int(input())

for _ in range(t):
    n, *numbers = map(int, input().split())  # 나머지는 리스트로 언패킹
    result = 0
    
    # 가능한 모든 쌍의 GCD를 계산하여 합산
    for i in range(n):
        for j in range(i + 1, n):
            result += math.gcd(numbers[i], numbers[j])
            
    print(result)