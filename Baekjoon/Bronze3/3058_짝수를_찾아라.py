t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    
    result = 0
    even_list = []
    
    for j in num:
        if j % 2 == 0:
            even_list.append(j)
            result += j
            
    print(result, min(even_list))