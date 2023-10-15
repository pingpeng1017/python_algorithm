n, m = map(int, input().split())

not_heard = set(input() for _ in range(n))
not_seen = set(input() for _ in range(m))

both = sorted(list(not_heard & not_seen))  # 교집합 구하기

print(len(both))

for i in both:
    print(i)