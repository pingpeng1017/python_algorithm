n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((y, x))  # y좌표를 기준으로 정렬

points.sort()

for point in points:
    print(point[1], point[0])  # x, y 순서로 출력