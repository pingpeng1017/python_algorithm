t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    # 0층의 각 호수에 사는 사람 수 초기화
    people = [i for i in range(1, n + 1)]

    # 1층부터 k층까지 계산
    for i in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]

    print(people[n - 1])