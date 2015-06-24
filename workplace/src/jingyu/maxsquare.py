def MaximalSquare(matrix):#bottom up
    if not matrix:
        return 0
    m=len(matrix)+1
    n=len(matrix[0])+1
    x=y=0
    max=0
    print m,n
    c=[[0 for i in range(n)]for j in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if int(matrix[i-1][j-1])==1:
                    c[i][j]=min(min(c[i][j-1],c[i-1][j]),c[i-1][j-1])+1
            else:
                c[i][j]=0
                
            if c[i][j]>max:
                max=c[i][j]
                x=i-1
                y=j-1
    for cc in c:
        print cc
    print x,y
    return max**2,[x-max+1,y-max+1,x-max+1,y,x,y-max+1,x,y]



matrix=[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

#matrix=["1"]
#matrix=['0']
#matrix=["11111111","11111110","11111110","11111000","01111000"]
for i in matrix:
    print i
print MaximalSquare(matrix)
