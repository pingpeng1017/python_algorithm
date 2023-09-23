t = int(input())
name = []
drink = []

for i in range(t):
    n = int(input())
    
    for j in range(n):
        s, l = input().split()
        name.append(s)
        drink.append(int(l))
        
    print(name[drink.index(max(drink))])