n = int(input())
list = list(map(int, input().split()))
sum = 0 
result = 0

for i in list:
    if i == 1:
        sum += 1
        result += sum
    else:
        sum = 0

print(result)