people = 0
result = []

for i in range(4):
    off, on = map(int, input().split())
    people += on
    people -= off
    result.append(people)
    
print(max(result))