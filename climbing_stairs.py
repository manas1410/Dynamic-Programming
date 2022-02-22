'''
Climbing Stairs
problem url : https://leetcode.com/problems/climbing-stairs/submissions/
'''
d = {}
def solve(n):
    if n in d:
        return d[n]
    d[n] = 0
    if n == 0 or  n ==1:
        d[n] = 1 
    else:
        d[n] = solve(n-1) +solve(n-2)
    return d[n]
solve(n)
