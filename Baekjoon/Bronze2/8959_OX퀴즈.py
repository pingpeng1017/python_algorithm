t = int(input())

for _ in range(t):
    ox = input()
    count = 0
    sum = 0
    
    for i in ox:
        if i == 'O':
            count += 1
            sum += count
        else:
            count = 0
            
    print(sum)