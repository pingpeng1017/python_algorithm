k = int(input())

a = 0
b = 1

# 2번째부터
for _ in range(1, k):
    a, b = b, a + b  # 피보나치 수열
    
print(a, b)