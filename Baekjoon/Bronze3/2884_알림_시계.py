h, m = map(int, input().split())

mins = h * 60 + m - 45

if mins < 0:
    mins += 24 * 60
    
new_h = mins // 60
new_m = mins % 60

print(new_h, new_m)