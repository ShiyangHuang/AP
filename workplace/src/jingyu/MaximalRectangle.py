def MaxRectangle(matrix):#bottom up
    if not matrix:
        return 0
    m=len(matrix)+1
    n=len(matrix[0])+1
    x=y=h=l=0
    max=0
    print m,n
    a=[[0 for i in range(n)]for j in range(m)]
    
    for i in range(1,m):
        for j in range(1,n):           
             a[i][j]=matrix[i-1][j-1]*(1+a[i-1][j])
    for  i,row in enumerate(a):
        print row
        result,yy,hh,ll=largestRectangle(row)
        if result>max:
            max=result
            x=i-1
            y=yy-1
            h=hh-1
            l=ll-1                        
    return max,[x-h,y-l,x-h,y,x,y-l,x,y]

def largestRectangle(height):
    height.append(0)
    stack = [0]
    area = 0
    y=h=l=0
    for i in range(1, len(height)):
        #print stack#,height[i],height[stack[-1]]
        while stack and height[i] < height[stack[-1]]:
            top = height[stack.pop()]
            w = i if not stack else i - stack[-1] -1
            if w*top>area:
                area = w*top
                y=i-1
                h=top
                l=w
        stack.append(i)
    return area,y,h,l


matrix=[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

#matrix=["1"]
#matrix=['0']
#matrix=["11111111","11111110","11111110","11111000","01111000"]
for i in matrix:
    print i
print MaxRectangle(matrix)
