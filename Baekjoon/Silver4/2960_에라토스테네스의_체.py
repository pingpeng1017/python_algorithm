n, k = map(int, input().split())
count = 0 
is_prime = [True] * (n + 1) # 소수 여부를 저장하는 리스트

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if is_prime[j] == True:
            is_prime[j] = False
            count += 1
            if count == k:
                print(j)
                break