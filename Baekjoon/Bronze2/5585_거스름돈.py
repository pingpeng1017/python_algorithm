n = int(input())
coins = [500, 100, 50, 10, 5, 1]
count = 0

change = 1000 - n

for coin in coins:
    num_coins = change // coin
    count += num_coins 
    change -= num_coins * coin
    
print(count)