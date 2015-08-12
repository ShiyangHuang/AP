class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):#O(n^2)
        count=0
        for i in range(n):
            if self.isPrime(i):
                count+=1
        return count
    def isPrime(self,x):
        if x<=1:return False
        for i in range(2,int(x**0.5)):
            if x%i==0:
                return False
        return True
#-------------------------------------
    def countPrimes2(self, n):#O(nlog(log(n)))
        count=0
        isPrime=[True for i in range(n)]
        for i in range(2,int(n**0.5)+1):
            if not isPrime[i]:
                continue
            st=i*i
            while st<n:
                isPrime[st]=False
                st+=i
        for i in range(2,n):
            if isPrime[i]:
                count+=1
        return count

#---------------------------------------
    def countPrimes3(self, n):#O(nlog(log(n))) 
        
        isPrime=[True]*n
        isPrime[:2]=[False]*2
        for i in range(2,int(n**0.5)+1):
            if not isPrime[i]:
                continue
            isPrime[i*i:n:i]=[True]*len(isPrime[i*i:n:i])

        return sum(isPrime)

s=Solution()
print s.countPrimes2(5)
