def Robber(nums):
    if not nums:
        return 0
    n=len(nums)
    if n<2:
        return nums[0]
    nums1=nums[:-1]
    nums2=nums[1:]
    
    index1=[None for i in range(n)]
    index2=[None for i in range(n)]
    
    r1=[0 for i in range(n)]
    r2=[0 for i in range(n)]
    r1[1]=nums1[0]
    r2[1]=nums2[0]
    index1[1]=1
    index2[1]=1
    for i in range(2,n):        
        r1[i]=max(nums1[i-1]+r1[i-2],r1[i-1])
        r2[i]=max(nums2[i-1]+r2[i-2],r2[i-1])
           
        if nums1[i-1]+r1[i-2]<=r1[i-1]:#record
            index1[i]=0
        else:
            index1[i]=1
        if nums2[i-1]+r2[i-2]<=r2[i-1]:#record
            index2[i]=0
        else:
            index2[i]=1
               
    if r1[n-1]>r2[n-1]:
        return r1[n-1],printlist(index1,nums1,0)
    else:              
        return r2[n-1],printlist(index2,nums2,1)

def printlist(index,nums,flag):
    print index
    n=len(nums)
    i=n-1
    a=[]
    b=[]
    print index
    while index:
        if index.pop()>0:
            index.pop()
            a.insert(0,nums[i])
            b.insert(0,i+flag)
            i-=2
        else:           
            i-=1
    return a,b



    

t=[1,2,3,4,5,1,2,3,4,5]
t=[1,2]

t=[1,2,4,1,2,3,4,5]

print Robber(t)
