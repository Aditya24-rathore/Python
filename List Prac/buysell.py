def profit(prices):
    profit=0
    buy = prices[0]
    for i in prices:
        if i < buy:
            buy=i
        else:
            pro=i-buy
            if pro > profit:
                profit=pro
    return profit

print(profit([2,1,3,5,7]))


