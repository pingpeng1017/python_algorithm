n = int(input())
count = 0

for i in range(1, n + 1):
    digits = []
    
    for j in str(i):
        digits.append(int(j))
    
    if i < 100:
        count += 1
    elif digits[1] - digits[0] == digits[2] - digits[1]:
        count += 1

print(count)      