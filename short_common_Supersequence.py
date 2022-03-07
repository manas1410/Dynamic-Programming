'''
problem url -: https://www.geeksforgeeks.org/shortest-common-supersequence/
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
print(len(x)+len(y) - t[len(x)][len(y)])
            
