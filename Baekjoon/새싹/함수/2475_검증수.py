n = map(int, input().split())
sum = 0

for i in n:
    num = i ** 2
    sum += num
    sum = sum % 10
    
print(sum)