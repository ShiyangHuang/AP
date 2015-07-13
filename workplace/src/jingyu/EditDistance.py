def minDistance(word1, word2):
    m,n=map(len,[word1,word2])
    #if m<n:return minDistance(word2, word1)
    c=[[None for j in range(n+1)] for i in range(m+1)]
    for j in range(n+1):
        c[0][j]=j
    for i in range(m+1):
        c[i][0]=i
    for i in range(1,m+1):
        for j in range(1,n+1):
            if  word1[i-1]==word2[j-1]:
                c[i][j]=c[i-1][j-1]
            else:
                c[i][j]=min(c[i-1][j-1],c[i-1][j],c[i][j-1])+1
  
    return c[m][n]

w1='ab'
w2='abdb'
print minDistance(w1, w2)
