def fib_like(n):
    if n <= 3:
        return 1
    
    a, b, c = 1, 1, 1

    # n이 4 이상인 경우
    for _ in range(n - 3):
        # f(n) = f(n-1) + f(n-3)
        a, b, c = b, c, a + c

    return c

n = int(input())

print(fib_like(n))