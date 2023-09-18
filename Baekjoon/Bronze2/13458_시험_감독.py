n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
total = 0

for num in a:
    num -= b
    total += 1
    
    if num > 0:
        if num % c == 0:
            total += num // c
        else:
            total += (num // c) + 1

print(total)