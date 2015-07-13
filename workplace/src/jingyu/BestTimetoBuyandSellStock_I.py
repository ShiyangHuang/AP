def maxProfit(prices):
    if len(prices)<2:
        return 0
    minprice=prices[0]
    profit=0
    temp,x,y=0,0,0
    
    for i in range(1,len(prices)):
        profit=max(profit,prices[i]-minprice)
        if profit==prices[i]-minprice:#index            
            y=i
            x=temp
        if prices[i]<minprice:
            minprice=prices[i]
            temp=i #index

    return profit,x,y,prices[x],prices[y]
        
        
a=[2,1,3,2,5,7]
a=[6,4]
print maxProfit(a)
