def isSubset(sumset,S,n):
    if S==0:
        return True
    if n<0 and S<>0:
        return False
    if sumset[n]>S:
        return issubset(sumset,S,n-1)
    return issubset(sumset,S-sumset[n],n-1) or issubset(sumset,S,n-1)
    
#--------------------------------------------------------------
def isSubset(sets,S):
    n=len(sets)

    c=[[None for i in range(S+1)] for i in range(n+1)]
    for i in range(n+1):c[i][0]=True
    for j in range(1,S+1): c[0][j]=False
    
    for i in range(1,n+1):
        for j in range(1,S+1):
            c[i][j]=c[i-1][j]
            if sets[i-1]<=j:
               c[i][j]=c[i][j]or c[i-1][j]or c[i-1][j-sets[i-1]]
 
    printitem(c,n,S,sets)       
    return c[n][S]
def printitem(c,i,j,sets):
    if i*j ==0:
        return
    if c[i][j]<>c[i-1][j]:
        printitem(c,i-1,j-sets[i-1],sets)
        print sets[i-1],
    else:
        printitem(c,i-1,j,sets)


#------------------------------------------------------
t=(1,[2,3])
t=(3,[1,2,5,6])
t=(9,[3,34,4,12,5,2])

print isSubset(t[0],t[1],len(t[0])-1)
print isSubset(t[0],t[1]):

