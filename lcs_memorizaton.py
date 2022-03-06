'''
problem url - https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
'''
def lcs(x,y,n,m):
    if dp[n][m]!=-1:
        return dp[n][m]
    if x[n-1] == y[m-1]:
        return t[n][m] = 1+lcs(x,y,n-1,m-1)
    else:
        return t[n][m] = max(lcs(x,y,n,m-1),lcs(x,y,n-1,m))
        
    
x=input()
y=input()
l=0
dp = [[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]
print(lcs(x,y,len(x),len(y)))
    
