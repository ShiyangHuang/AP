def longestPalindrome(s): #brute force
    maxsub=''
    if len(s)<2:
        return s
    for i in range(len(s)):
        j=i+1
        while j<len(s):
            if s[j]==s[i]:
                mid=(j-i)/2
                a,b,stop=i,j,1
                while stop and a<=mid and b>=mid:
                    if s[a]<>s[b]:
                        stop=0
                        continue
                    a+=1
                    b-=1
                if stop and j-i+1>len(maxsub):
                    maxsub=s[i:j+1]
            j+=1
    return maxsub

def longestPalindrome2(s):
    n=len(s)+1
    c=[[0 for i in range(n)] for j in range(n)]
    p,x=0,0
    maxsub=''
    for i in range(1,n):
        for j in range(1,n):
            k=n-j-2  #reverse
            if s[i-1]==s[k+1]:
                c[i][j]=c[i-1][j-1]+1
                if c[i][j]>p:
                    p=c[i][j]
                    x=i
   
    return s[x-p:x]
                
def longestPalindrome3(s):
    if len(s)==0:
            return 0
    maxlen=1
    st=0
    for i in xrange(1,len(s)):
            if i-maxlen >=1 and s[i-maxlen-1:i+1]==s[i-maxlen-1:i+1][::-1]:  # x [----size------] x
                st=i-maxlen-1
                maxlen+=2
                continue

            if i-maxlen >=0 and s[i-maxlen:i+1]==s[i-maxlen:i+1][::-1]:     # [x----size------] x
                st=i-maxlen
                maxlen+=1
    return s[st:st+maxlen]


    
x='aaabaa'

print longestPalindrome2(x)
            
                
            
