while True:
    a, b, c = map(int, input().split())
    a, b, c = sorted([a, b, c])
    
    if a == b == c == 0:
        break
    if a + b <= c:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")