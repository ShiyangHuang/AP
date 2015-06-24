def issubset(sumset,S,n):
    if S==0:
        return True
    if n<0 and S<>0:
        return False
    if sumset[n]>S:
        return issubset(sumset,S,n-1)
    return issubset(sumset,S-sumset[n],n-1) or issubset(sumset,S,n-1)
    

def run(sumset,S):
    print issubset(sumset,S,len(sumset)-1)


t=(1,[2,3])
t=(3,[1,2,5,6])
t=(9,[3,34,4,12,5,2])


run(t[1],t[0])
