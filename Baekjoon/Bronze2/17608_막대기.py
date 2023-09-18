import sys

n = int(sys.stdin.readline())
heights = []

for _ in range(n):
    h = int(sys.stdin.readline())
    heights.append(h)

count = 1
max_height = heights[-1]

for i in range(n - 2, -1, -1):
    if heights[i] > max_height:
        count += 1
        max_height = heights[i]

print(count)