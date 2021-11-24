prices = list(map(lambda x: int(x), open('INPUT.TXT').read().split()))
n = prices.pop(0)
length = 1
money = 0

for i in range(n-1):
    if prices[i] != max(prices[i::]):
        length += 1

    else:
        money += length * prices[i]
        length = 1

money += length * prices[n-1]
open('OUTPUT.TXT', 'w').write(str(money))