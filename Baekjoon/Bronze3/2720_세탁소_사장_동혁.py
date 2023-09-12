t = int(input())
quarters = 0
dimes = 0
nickels = 0
pennies = 0

for i in range(t):
    c = int(input())
    quarters = c // 25
    c %= 25
    dimes = c // 10
    c %= 10
    nickels = c // 5
    c %= 5
    pennies = c
    print(quarters, dimes, nickels, pennies)