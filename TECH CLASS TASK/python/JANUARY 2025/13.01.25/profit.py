n=int(input())
prices=[]
for i in range(n):
    prices.append(int(input()))
profit = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
print(profit)

