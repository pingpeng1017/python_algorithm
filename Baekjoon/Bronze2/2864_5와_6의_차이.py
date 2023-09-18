a, b = map(int, input().split())

min_sum = int(str(a).replace('6', '5')) + int(str(b).replace('6', '5'))
max_sum = int(str(a).replace('5', '6')) + int(str(b).replace('5', '6'))

print(min_sum, max_sum)