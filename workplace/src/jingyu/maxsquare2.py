class maxsquare2:
    # @param {character[][]} matrix
    # @return {integer}
    c=[]
    def MSS(self,matrix):
        if not matrix:
            return 0
        m=len(matrix)+1
        n=len(matrix[0])+1
        x=y=0
        max=0
        print m,n
        self.c=[[0 for i in range(n)]for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
               result=self.MS(matrix,i,j)
               if result>max:
                    max=result
                    x=i-1
                    y=j-1
        
        for cc in self.c:
           print cc
        return max**2,[x-max+1,y-max+1,x-max+1,y,x,y-max+1,x,y]
        
    def MS(self,matrix,i,j):#Topdown up
        if i*j==0:
            return 0       
        if self.c[i][j]>0:
            return self.c[i][j]
        if int(matrix[i-1][j-1])==1:
            self.c[i][j]=min(min(self.MS(matrix,i-1,j),self.MS(matrix,i,j-1)),self.MS(matrix,i-1,j-1))+1
        else:
            self.c[i][j]=0
        return self.c[i][j]


matrix=[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
matrix=["000","000","000","000"]
#matrix=["1"]
#matrix=['0']
#matrix=["11111111","11111110","11111110","11111000","01111000"]
for i in matrix:
    print i
m=maxsquare2()
print m.MSS(matrix)
