

def Robber(nums):
    if not nums:
        return 0
    n=len(nums)
    index=[1 for i in range(n)]
    r=[0 for i in range(n)]
    a=[]
    b=[]
    r[1]=nums[0]
    for i in range(2,n):       
        r[i]=max(nums[i-1]+r[i-2],r[i-1])
        if nums[i-1]+r[i-2]<=r[i-1]:
            index[i-1]=0
    i=n-1
    index.insert(0,None)
    while index:
        if index.pop()>0:
            index.pop()
            a.insert(0,nums[i])
            b.insert(0,i)
            i-=2
        else:
            i-=1
            
    return r[n-1],a,b


print Robber([1,2,3,4,5,1,2,3,4,5])
#----------------------------------------------------------------

def Robber(nums,i):
    if not nums:
        return 0
    if i<0:
        return 0
    if i==0:
        return nums[0]

    if nums[i]+Robber(nums,i-2)<=Robber(nums,i-1):#record
        index[i]=0               
    return max(nums[i]+Robber(nums,i-2),Robber(nums,i-1))

def printlist(nums,i):
    index.insert(0,None)
    while index:
       # print index,a
        if index.pop()>0:
            index.pop()
            a.insert(0,nums[i])
            b.insert(0,i)
            i-=2
        else:
            i-=1
    return a,b



nums=[1,2,3,4,5,1,2,3,4,5]
a=[]
b=[]
index=[1 for i in range(len(nums))]
print Robber(nums,len(nums)-1)
#print index
print printlist(nums,len(nums)-1)


    
            
    
