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
