n = int(input())
name_set = set()

for _ in range(n):
    name, status = map(str, input().split())
    if status == 'enter':
        name_set.add(name)
    else:
        name_set.discard(name)
    
sorted_names = sorted(name_set, reverse=True)

for name in sorted_names:
    print(name)