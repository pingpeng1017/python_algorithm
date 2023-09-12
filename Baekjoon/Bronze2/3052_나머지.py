a = []

for i in range(10):
    num = int(input())
    a.append(num % 42)
    
a = set(a)
print(len(a))