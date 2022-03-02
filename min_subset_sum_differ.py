'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 

problem url - https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
'''

t=[[]]
arr=[1, 6, 11, 5]
sums = sum(arr)
t = [[False for j in range(sums+1)] for j in range(len(arr)+1)]
l = []
for i in range(len(arr)+1):
    for j in range(sums+1):
        if i ==0:
            t[i][j]=False
        if j == 0:
            t[i][j]=True
            
def subsetsum(arr,sums):
    for i in range(1,len(arr)+1):
        for j in range(sums+1):
            if arr[i-1]>j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] =  t[i-1][j-arr[i-1]] or t[i-1][j]
    for i in range((sums+1)//2 +1):
        if t[len(arr)-1][i]:
            l.append(i)
 
  
    
subsetsum(arr,sums)
mins = sums
#print(t)
#print(l)
for i in l:
    mins = min(mins,sums-2*i)
print(mins)
