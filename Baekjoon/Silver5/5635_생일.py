n = int(input())

list = []

for _ in range(n):
    student = input().split()
    name = student[0]
    day = int(student[1])
    month = int(student[2])
    year = int(student[3])
    list.append([year, month, day, name])

list.sort()

print(list[-1][3])
print(list[0][3])