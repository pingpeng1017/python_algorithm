l, p = map(int, input().split())
n = list(map(int, input().split()))
person = l * p

for i in n:
    print(i - person , end = " ")