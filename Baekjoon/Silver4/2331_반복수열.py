a, p = map(int, input().split())
d = [a]

while True:
    next_num = 0
    for i in str(d[-1]):  
        next_num += int(i) ** p
        
    if next_num in d:
            break
        
    d.append(next_num)

print(d.index(next_num))