#this program will say true is subset sum is present and False if not pResent
#problem url -  https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

t=[[]]
arr=[2,3,8,10]
sums = 6
t = [[False for j in range(sums+1)] for j in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(sums+1):
        if i ==0:
            t[i][j]=False
        if j == 0:
            t[i][j]=True
            
def subsetsum(arr,sums):
    for i in range(len(arr)+1):
        for j in range(sums+1):
            if arr[i-1]>j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] =  t[i-1][j-arr[i-1]] or t[i-1][j]
    return t[len(arr)][sums] 
  
    
print(subsetsum(arr,sums))
