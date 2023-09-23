mushrooms = []
total = 0

for _ in range(10):
    score = int(input())
    mushrooms.append(score)

for score in mushrooms:
    total += score
    if total >= 100:
        break

if (total - 100) > (100 - (total - score)):
    total -= score

print(total)