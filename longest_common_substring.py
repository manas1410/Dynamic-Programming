'''
problem url :- https://www.geeksforgeeks.org/longest-common-substring-dp-29/
'''

x=input() 
y=input() 
l=0
t = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
res= 0
for i in range(1,len(x)+1):
    for j in range(1,len(y)+1):
        if x[i-1] == y[j-1]:
            t[i][j] = t[i-1][j-1]+1
            res = max(res,t[i][j])
        else:
            t[i][j] = 0
print(res)
