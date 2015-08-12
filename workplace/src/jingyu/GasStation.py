class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if sum(gas)<sum(cost):
            return -1
        start=tank=0
        for i in range(len(gas)):
            tank=tank+gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        return start
            
                
s=Solution()
print s.canCompleteCircuit([2],[2])
            
        
##rule1:
##    A--(c1)---B---(c2)---C-----(c3)----D
##    if A Can not reach D
##    then B,C can not reach D either
##
##    prove:
##        since:
##            g1-c1>0
##            g1+g2-c1-c2>0
##            g1+g2+g3-c1-c2-c3<0
##        then g3-c3<0 C cannot reach D
##        then g2+g3-c2-c3<0 B cannot reach D

            
##    
##rule2:
##     A-----B------C--------D-----A
##     if g1+g2+g3+g4>c1+c2+c3+c4:
##         g1+g2+g3+g4-c1-c2-c3-c4>0
##     there musct be a solution if Sum(gas)> Sum(cost)
