from __future__ import division
from math import sqrt
from heapq import heappush, heappop

def printTransactions(money, k, d, name, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = mean(nums)
        return sqrt(sum((x - average) ** 2 for x in nums) / len(nums))

    def info(price):
        mu = mean(price)
        sigma = sd(price)
        trend = (price[-1] - price[-2]) / price[-2] if price[-2] != 0 else 0
        up_trends = sum(price[i] > price[i - 1] for i in range(1, 5))
        
        return trend
    
    infos = [info(p) for p in prices]
    res = []
    
    drop = []
    
    for i in range(k):
        cur_info = infos[i]
        if cur_info > 0 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
        elif cur_info < 0:
            heappush(drop, (cur_info, i, name[i]))
    
    while money > 0.0 and drop:
        rate, idx, n = heappop(drop)
        price = prices[idx][-1]
        amount = int(money / price)
        if amount > 0:
            res.append((n, 'BUY', str(amount)))
            money -= amount * price
    
    print(len(res))
    for r in res:
        print(' '.join(r))

if __name__ == '__main__':
    m, k, d = map(float, input().strip().split())
    k = int(k)
    d = int(d)
    
    names = []
    owned = []
    prices = []
    
    for _ in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])
    
    printTransactions(m, k, d, names, owned, prices)
