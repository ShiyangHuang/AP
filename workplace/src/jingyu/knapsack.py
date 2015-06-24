def knapsack(v,w,S):
    m=len(v)
    c=[[0 for i in range(S+1)] for j in range(m+1)]
    b=[[0 for i in range(S+1)] for j in range(m+1)]   
    for i in range(1,m+1):
        for j in range(1,S+1):
            if w[i-1]>j:
                c[i][j]=c[i-1][j]
                b[i][j]=0
            elif v[i-1]+c[i-1][j-w[i-1]]>c[i-1][j]:
                c[i][j]=v[i-1]+c[i-1][j-w[i-1]]
                b[i][j]=1
            else:
                c[i][j]=c[i-1][j]
                b[i][j]=0

    printitem(b,m,S,w,v)
    return c[m][S]
def printitem(b,i,j,w,v):
    if i==0 or j==0:
        return
    if b[i][j]>0:
        printitem(b,i-1,j-w[i-1],w,v)
        print w[i-1],v[i-1]
    else:
        printitem(b,i-1,j,w,v)
    

v=[40,35,18,4,10,2]
w=[100,50,45,20,10,5]
W=100

w=[1,2,3,2,2]
v=[8,4,0,5,3]
S=4
print knapsack(v,w,S)
