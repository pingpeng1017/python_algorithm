t = int(input())

for _ in range(t):
    n = int(input())
    n_set = set(map(int, input().split()))
    m = int(input())
    m_set = list(map(int, input().split()))

    for i in m_set:
        if i in n_set:
            print(1)
        else:
            print(0)