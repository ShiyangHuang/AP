class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        count=0
       
        sign=-1 if dividend*divisor<0 else 1
        dividend,divisor=map(abs,[dividend,divisor])
        while dividend>=divisor:
            d=divisor
            step=1           
            while((d<<1)<dividend):
                d<<=1
                step<<=1
            dividend-=d
            count+=step           
        return  min(sign*count,2147483647)

    
s=Solution()
print s.divide(-2147483648, -1)
