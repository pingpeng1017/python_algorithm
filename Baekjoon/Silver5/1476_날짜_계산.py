e, s, m = map(int, input().split())
a, b, c = 1, 1, 1
year = 1

while True :
    if e == a and s == b and m == c:
        break
    year += 1
    a += 1
    b += 1
    c += 1
    
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1
    
print(year)


# e, s, m = map(int, input().split())
# year = 1

# while True:
#     if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
#         break
#     year += 1

# print(year)