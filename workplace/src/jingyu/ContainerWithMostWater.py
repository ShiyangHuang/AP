class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        area=0
        head,tail=0,len(height)-1
        while head<tail:
            area=max(area,(tail-head)*min(height[head],height[tail]))
            if height[head]>height[tail]:
                tail-=1
            else:
                head+=1
        
        return area


s=Solution()

print s.maxArea2([1,2,4,3])

#idea:
##step1 (O(N^2)/2)
##      1 2 3 4 5 
##    1 x 
##    2 x x
##    3 x x x
##    4 x x x x
##    5 x x x x x

##step2:(O(N))
##    al<ar: move al->
##    ar<al: move <-ar
##    prove: if al<ar then min(al,ax)*dlx <al*dlr  because dlx<dlr
##    so we can skip the computations for al--ax x<r


