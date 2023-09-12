a = int(input())
b = int(input())
c = int(input())
total = a + b + c

if total == 180:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a ==c:
        print("Isosceles")
    elif a != b or b != c or a !=c:
        print("Scalene")
else:
    print("Error")