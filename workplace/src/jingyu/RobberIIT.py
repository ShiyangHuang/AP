def run(nums):
    n=len(nums)-1
    index1=[1 for i in range(n)]
    index2=[1 for i in range(n)]
    result1=Robber(nums[1:],n-1,index1)
    result2=Robber(nums[:-1],n-1,index2)
    if result1>result2:
        print result1,printlist(nums[1:],n-1,index1)
    else:
        print result2,printlist(nums[:-1],n-1,index2)


def Robber(nums,i,index):
    if not nums:
        return 0
    if i<0:
        return 0
    if i==0:
        return nums[0]

    if nums[i]+Robber(nums,i-2,index)<=Robber(nums,i-1,index):#record
        index[i]=0               
    return max(nums[i]+Robber(nums,i-2,index),Robber(nums,i-1,index))

def printlist(nums,i,index):
    a=[]
    b=[]
    index.insert(0,None)
    while index:
       # print index,a
        if index.pop()>0:
            index.pop()
            a.insert(0,nums[i])
            b.insert(0,i+1)
            i-=2
        else:
            i-=1
    return a,b



nums=[1,2,3,4,5,1,2,3,4,5]
nums=[1,2]
nums=[1,2,4,1,2,3,4,5]
run(nums)
