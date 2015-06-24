def largestRectangle(height):
    height.append(0)
    stack = [0]
    area = 0
    x=y=l=0
    for i in range(1, len(height)):
        #print stack#,height[i],height[stack[-1]]
        while stack and height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i if not stack else i - stack[-1] -1
            if w*h>area:
                area = w*h
                x=i-1
                y=h
                l=w
            
            #print h,w, area
        stack.append(i)
    return area,x,y,l

height=[2,1,5,6,2,3]
#height=[1,2,3,4,5,1,2,3,1]
print largestRectangle(height)
