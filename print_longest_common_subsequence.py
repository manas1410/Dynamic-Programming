'''
problem url:- https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
'''
x=input() 
y=input() 
l=0
t = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1] == y[j-1]:
            t[i][j] = t[i-1][j-1]+1
            
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
i=len(x)
j=len(y)
res = ''
while(i>0 and j>0):
    if x[i-1] == y[j-1]:
        res+=x[i-1]
        i-=1 
        j-=1 
    else:
        if t[i][j-1]>t[i-1][j]:
            j-=1 
        else:
            i-=1
print(res[::-1])
    
