'''
Input : 1,1,2,3 diff = 1
Output: 3
explaination :
   1st 1+2 and 3+1
   2nd 1+2 and 3+1
   3rd 1+1+2 and 3
   
'''

t=[[]]
arr=[1,1,2,3]
diff = 1 
sums = (diff+sum(arr))//2
t = [[0 for j in range(sums+1)] for j in range(len(arr)+1)]

for i in range(len(arr)+1):
    for j in range(sums+1):
        if i ==0:
            t[i][j]=0
        if j == 0:
            t[i][j]=1
            
def subsetsum(arr,sums):
    for i in range(1,len(arr)+1):
        for j in range(sums+1):
            if arr[i-1]<=j: 
                t[i][j] =  t[i-1][j] + t[i-1][j-arr[i-1]]
            else:
                t[i][j] =  t[i-1][j]
    return t[len(arr)][sums] 
  
    
print(subsetsum(arr,sums))
