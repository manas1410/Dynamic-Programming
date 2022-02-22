'''
problem url : https://leetcode.com/problems/fibonacci-number/
'''
d = {}
def solve(n):
    if n in d.keys():
        return d[n]
    d[n] = 0
    if n==1 or n==2:
        d[n] = 1
    elif n!=0:
        d[n] =solve(n-1)+solve(n-2)
    return d[n]
return solve(n)
