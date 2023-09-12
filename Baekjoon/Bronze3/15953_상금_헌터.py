t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    prize_2017 = 0
    if 1 <= a <= 21:
        if a == 1:
            prize_2017 = 5000000
        elif 2 <= a <= 3:
            prize_2017 = 3000000
        elif 4 <= a <= 6:
            prize_2017 = 2000000
        elif 7 <= a <= 10:
            prize_2017 = 500000
        elif 11 <= a <= 15:
            prize_2017 = 300000
        elif 16 <= a <= 21:
            prize_2017 = 100000

    prize_2018 = 0
    if 1 <= b <= 31:
        if b == 1:
            prize_2018 = 5120000
        elif 2 <= b <= 3:
            prize_2018 = 2560000
        elif 4 <= b <= 7:
            prize_2018 = 1280000
        elif 8 <= b <= 15:
            prize_2018 = 640000
        elif 16 <= b <= 31:
            prize_2018 = 320000

    total_prize = prize_2017 + prize_2018
    print(total_prize)